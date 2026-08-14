import pandas as pd
import numpy as np

# 固定随机种子，保证结果可复现
np.random.seed(42)
n = 300  # 样本总量

# ---------------------- 1. 基础信息与甄别题 ----------------------
data = {'S1_甄别': ['是'] * n}

# Q1 性别
data['Q1_性别'] = np.random.choice(['男', '女'], size=n, p=[0.42, 0.58])

# Q2 年龄段
data['Q2_年龄段'] = np.random.choice(
    ['18岁及以下', '19-35岁', '36-59岁', '60岁以上'],
    size=n, p=[0.08, 0.72, 0.17, 0.03]
)

# Q3 地区
data['Q3_所在地区'] = np.random.choice(
    ['江西省内', '国内其他省份'], size=n, p=[0.35, 0.65]
)

# Q4 学历
data['Q4_最高学历'] = np.random.choice(
    ['高中及以下', '大专/本科', '硕士及以上'],
    size=n, p=[0.12, 0.78, 0.10]
)

# Q5 月可支配收入
data['Q5_月可支配收入'] = np.random.choice(
    ['2000元及以下', '2001-4000元', '4001-6000元', '6001-8000元', '8000元以上'],
    size=n, p=[0.28, 0.35, 0.22, 0.10, 0.05]
)

# Q6 是否购买过鸭鸭
buy_exp = np.random.choice(
    ['购买并使用过', '没买过，但听说过', '完全没听说过'],
    size=n, p=[0.45, 0.48, 0.07]
)
data['Q6_是否购买过鸭鸭'] = buy_exp

# ---------------------- 2. 多选题（拆分为0-1变量） ----------------------
# Q7 了解渠道
q7_options = ['电商平台', '线下门店', '亲友推荐', '社交媒体', '直播带货', '其他']
q7_probs = [0.75, 0.30, 0.40, 0.65, 0.55, 0.10]
for opt, prob in zip(q7_options, q7_probs):
    col = f'Q7_了解渠道_{opt}'
    data[col] = np.random.binomial(1, prob, size=n)
# 完全没听过的人，渠道全为0
mask_unknown = buy_exp == '完全没听说过'
for opt in q7_options:
    data[f'Q7_了解渠道_{opt}'][mask_unknown] = 0

# Q8 选购看重因素（限选3项）
q8_options = ['保暖性能', '价格', '款式设计', '品牌口碑', '填充物品质',
              '国潮/国风设计元素', '本土国货品牌属性', '售后服务']
q8_weights = [0.25, 0.20, 0.18, 0.12, 0.13, 0.05, 0.04, 0.03]
q8_data = np.zeros((n, len(q8_options)), dtype=int)
for i in range(n):
    selected = np.random.choice(len(q8_options), size=3, replace=False, p=q8_weights)
    q8_data[i, selected] = 1
for idx, opt in enumerate(q8_options):
    data[f'Q8_看重因素_{opt}'] = q8_data[:, idx]

# ---------------------- 3. 行为类单选题 ----------------------
# Q9 预算区间
data['Q9_常规预算'] = np.random.choice(
    ['300元以内', '301-600元', '601-1000元', '1001-1500元', '1500元以上'],
    size=n, p=[0.15, 0.40, 0.30, 0.12, 0.03]
)

# Q10 购买频率
data['Q10_购买频率'] = np.random.choice(
    ['1年以内', '1-2年', '2-3年', '3年以上'],
    size=n, p=[0.18, 0.42, 0.30, 0.10]
)

# ---------------------- 4. 李克特量表（带组间差异与相关性） ----------------------
# 个体整体态度倾向，用于制造变量间的正相关
individual_trait = np.random.normal(0, 0.5, size=n)
# 分组均值调整：购买过的+0.4分，听说过的+0.1分，没听过的-0.2分
group_adjust = np.where(buy_exp == '购买并使用过', 0.4,
                       np.where(buy_exp == '没买过，但听说过', 0.1, -0.2))

# 生成分数的工具函数（限制1-5分）
def likert_score(base_mean, std=0.8, trait_weight=0.6):
    scores = base_mean + group_adjust + individual_trait * trait_weight + np.random.normal(0, std, size=n)
    return np.clip(np.round(scores), 1, 5).astype(int)

# 国潮文化符号感知 Q11-Q15
data['Q11_国风款式设计有吸引力'] = likert_score(3.2)
data['Q12_了解国潮联名产品'] = likert_score(2.9)
data['Q13_品牌体现东方美学'] = likert_score(3.1)
data['Q14_传统文化元素产生认同'] = likert_score(3.3)
data['Q15_国潮提升品牌好感度'] = likert_score(3.4)

# 本土制造认同 Q16-Q20
data['Q16_江西本土制造品质可信'] = likert_score(3.6)
data['Q17_本土品牌增加亲切感'] = likert_score(3.5)
data['Q18_愿意支持本土产业'] = likert_score(3.3)
data['Q19_更信任国货质量售后'] = likert_score(3.4)
data['Q20_本土标签提升认可度'] = likert_score(3.5)

# 品牌忠诚度 Q21-Q26
data['Q21_同价位优先选鸭鸭'] = likert_score(3.1)
data['Q22_相信品牌品质宣传'] = likert_score(3.3)
data['Q23_有情感偏好不轻易换'] = likert_score(3.0)
data['Q24_未来有复购意愿'] = likert_score(3.4)
data['Q25_愿意推荐给亲友'] = likert_score(3.3)
data['Q26_价格小幅上涨仍购买'] = likert_score(2.9)

# ---------------------- 5. 开放建议题 ----------------------
suggest_pool = [
    "", "", "", "", "", "", "",
    "希望多出简约国风款",
    "保暖性可以再提升",
    "价格再亲民一点",
    "线下门店太少了",
    "可以多结合江西文化做设计",
    "款式有点老气",
    "填充物信息更透明就好了",
    "支持本土品牌，加油"
]
data['Q27_开放建议'] = np.random.choice(suggest_pool, size=n,
                                        p=[0.7, 0.05, 0.03, 0.03, 0.03,
                                           0.03, 0.02, 0.02, 0.02, 0.02,
                                           0.02, 0.02, 0.01, 0.01, 0.01])

# ---------------------- 6. 整理并导出Excel ----------------------
df = pd.DataFrame(data)

# 按问卷顺序排列列名
col_order = [
    'S1_甄别',
    'Q1_性别', 'Q2_年龄段', 'Q3_所在地区', 'Q4_最高学历', 'Q5_月可支配收入',
    'Q6_是否购买过鸭鸭',
    'Q7_了解渠道_电商平台', 'Q7_了解渠道_线下门店', 'Q7_了解渠道_亲友推荐',
    'Q7_了解渠道_社交媒体', 'Q7_了解渠道_直播带货', 'Q7_了解渠道_其他',
    'Q8_看重因素_保暖性能', 'Q8_看重因素_价格', 'Q8_看重因素_款式设计',
    'Q8_看重因素_品牌口碑', 'Q8_看重因素_填充物品质', 'Q8_看重因素_国潮/国风设计元素',
    'Q8_看重因素_本土国货品牌属性', 'Q8_看重因素_售后服务',
    'Q9_常规预算', 'Q10_购买频率',
    'Q11_国风款式设计有吸引力', 'Q12_了解国潮联名产品', 'Q13_品牌体现东方美学',
    'Q14_传统文化元素产生认同', 'Q15_国潮提升品牌好感度',
    'Q16_江西本土制造品质可信', 'Q17_本土品牌增加亲切感', 'Q18_愿意支持本土产业',
    'Q19_更信任国货质量售后', 'Q20_本土标签提升认可度',
    'Q21_同价位优先选鸭鸭', 'Q22_相信品牌品质宣传', 'Q23_有情感偏好不轻易换',
    'Q24_未来有复购意愿', 'Q25_愿意推荐给亲友', 'Q26_价格小幅上涨仍购买',
    'Q27_开放建议'
]
df = df[col_order]

# 导出xlsx文件
df.to_excel('鸭鸭羽绒服调研模拟数据300份.xlsx', index=False)
print("数据文件已生成：鸭鸭羽绒服调研模拟数据300份.xlsx")