# 開源盤古 Ultra-MoE-718B
中文 | [English](README_EN.md)

## 1. 簡介
openPangu-Ultra-MoE-718B 是基於昇騰NPU從零訓練的大規模混合專家語言模型，總參數量為718B，激活參數量為39B。openPangu-Ultra-MoE-718B 訓練了約19T tokens，具備快慢思考融合能力。

## 2. 模型架構
openPangu-Ultra-MoE-718B 的模型架構採用了業界主流的Multi-head Latent Attention (MLA)、Multi-Token Prediction (MTP)、大稀疏比等架構，以及一些特有的設計：

- Depth-Scaled Sandwich-Norm和TinyInit：通過調整層歸一化結構與參數初始化，提升訓練穩定性。
- 基於EP-Group的負載均衡策略：通過優化負載均衡損失函數，改善專家特化效果。

## 3. 測評結果

|       測評集        |             測評指標             |  慢思考  |
|:----------------:|:----------------------------:|:-----:|
|     **通用能力**     |                              |       |
|      C-Eval      |             Acc              | 91.06 |
|     CLUEWSC      |             Acc              | 94.67 |
|     MMLU-Pro     |         Exact Match          | 82.40 |
|  ArenaHard_v0.1  |      w/o Style Control       | 96.80 |
|   GPQA-Diamond   |            Avg@4             | 76.77 |
|    SuperGPQA     |             Acc              | 61.67 |
|     IF-Eval      |        Prompt Strict         | 80.59 |
|     SysBench     | Constraint Satisfaction Rate | 91.43 |
|     **數學能力**     |                              |       |
|    CNMO 2024     |            Avg@32            | 80.73 |
|      AIME25      |            Avg@16            | 75.21 |
|      AIME24      |            Avg@16            | 80.21 |
|     MATH-500     |            Avg@1             | 97.40 |
|     **代碼能力**     |                              |       |
|   LiveCodeBench  |     Avg@3 (01/25~05/25)      | 61.14 |
|      MBPP+       |            Avg@2             | 81.48 |

**注：** 評測過程中，system prompt 為空。


## 4. 部署和使用
### 4.1 環境準備
#### 硬件規格
Atlas 800T A2 (64GB, >=32卡)，驅動與固件安裝包獲取請參照[[Atlas 800T A2](https://www.hiascend.com/hardware/firmware-drivers/community?product=4&model=26&cann=8.2.RC1.alpha003&driver=Ascend+HDK+25.0.RC1)]

#### 軟件環境
- 方式一：基於裸機環境安裝以下配套軟件
  - 操作系統：Linux（推薦openEuler>=24.03）
  - CANN==8.1.RC1，安裝準備及流程請參照[[CANN Install](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/82RC1alpha002/softwareinst/instg/instg_0001.html?Mode=PmIns&OS=Ubuntu&Software=cannToolKit)]
  - python==3.10
  - torch==2.1.0
  - torch-npu==2.1.0.post12
  - transformers>=4.48.2

- 方式二：從docker鏡像啟動容器 
  
  參考[[Docker使用指南](doc/docker.md)]

以上軟件配套經過驗證，理論可以支持更高的版本，如有疑問，可以提交issue。

### 4.2 權重完整性校驗
請參考以下方法對下載內容進行完整性校驗，hash 值存儲在 checklist.chk 文件中。

```
#!/usr/bin/env bash
ARCH=$(uname -m)
MODEL_PATH="${TARGET_FOLDER}/${MODEL_FOLDER_PATH}"
cd "$MODEL_PATH" || exit 1
if [ "$ARCH" = "arm64" ]; then
    sha256sum checklist.chk
else
    sha256sum -c checklist.chk
fi
```

### 4.3 推理權重轉換
本次樣例 openPangu-Ultra-MoE-718B 推理採用 Tensor Parallel 並行策略，疊加昇騰 NPU 融合大算子，需要提前對 safetensors 權重進行切分，下述內容提供32卡並行推理的權重切分示例，切分後的權重會保存在`model/`目錄下：
```bash
cd inference
bash split_weight.sh
```

### 4.4 推理樣例
openPangu-Ultra-MoE-718B 在 Atlas 800T A2 上4機32卡bfloat16推理示例，主節點選取節點IP0：
```bash
cd inference
# 主節點IP0:  ${NNODES} ${NODE_RANK} ${NPROC_PER_NODE} ${MASTER_ADDR} ${PROMPT}
bash generate.sh 4 0 8 IP0 "3*7=?"
# 從節點IP1
bash generate.sh 4 1 8 IP0 "3*7=?"
# 從節點IP2
bash generate.sh 4 2 8 IP0 "3*7=?"
# 從節點IP3
bash generate.sh 4 3 8 IP0 "3*7=?"
```
模型默認為慢思考模式，可以通過以下手段切換至快思考模式：如`generate.py`示例中`fast_thinking_template`所示，在用戶輸入結尾添加` /no_think`標記可以將當前輪次切換至快思考模式。

### 4.5 使用推理框架
vllm_ascend：參考[[vllm_ascend_for_openPangu_ultra_moe_718b](doc/vllm_ascend_for_openpangu_ultra_moe_718b.md)]

## 5. 模型許可證
除文件中對開源許可證另有約定外，openPangu-Ultra-MoE-718B 模型根據 OPENPANGU MODEL LICENSE AGREEMENT VERSION 1.0 授權，旨在允許使用並促進人工智能技術的進一步發展。有關詳細信息，請參閱模型存儲庫根目錄中的 [LICENSE](LICENSE) 文件。

## 6. 免責聲明
由於 openPangu-Ultra-MoE-718B （“模型”）所依賴的技術固有的限制，以及人工智能生成的內容是由盤古自動生成的，華為無法對以下事項做出任何保證：
- 該模型的輸出通過AI算法自動生成，不能排除某些信息可能存在缺陷、不合理或引起不適的可能性，生成的內容不代表華為的態度或立場； 
- 無法保證該模型100%準確、可靠、功能齊全、及時、安全、無錯誤、不間斷、持續穩定或無任何故障； 
- 該模型的輸出內容不構成任何建議或決策，也不保證生成的內容的真實性、完整性、準確性、及時性、合法性、功能性或實用性。生成的內容不能替代醫療、法律等領域的專業人士回答您的問題。生成的內容僅供參考，不代表華為的任何態度、立場或觀點。您需要根據實際情況做出獨立判斷，華為不承擔任何責任。

## 7. 反饋
如果有任何意見和建議，請提交issue或聯繫[openPangu@huawei.com](url)。