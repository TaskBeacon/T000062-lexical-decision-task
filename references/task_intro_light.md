# 视觉词汇判断任务：词汇通达、证据积累及其测量边界

视觉词汇识别研究需要回答一个基本问题：读者如何由字母串的视觉形式迅速获得其词汇身份，并在词形、语音和语义信息相互制约的条件下作出可观察的判断。词汇判断任务（lexical decision task, LDT）将这一问题操作化为二选一分类，即判断所呈现的字母串是否为真实词。反应时、正确率及其分布由此成为考察词汇性、词频、正字法邻近性和语义启动效应的主要指标。该任务结构简洁且易于扩展，但一次“词/非词”反应同时包含视觉编码、词汇证据形成、决策标准设置和运动执行。因此，LDT 更适合用于检验经明确操控的条件差异，而不宜把反应时直接等同于纯粹的词汇通达时间。

## 1. 范式提出与理论背景

早期研究以词和可发音非词的分类考察内部词典的组织。Rubenstein、Garfield 和 Millikan（1970）利用词汇判断比较同形词与单义词，显示该范式能够在不要求朗读或释义的情况下测量词汇表征的可用性。Meyer 和 Schvaneveldt（1971）随后以成对字母串证明，语义相关词对的判断快于无关词对，使 LDT 成为研究语义启动及词汇网络组织的重要方法。Forster 和 Chambers（1973）进一步比较命名与词汇判断，发现高频词在两种任务中均具反应优势，由此推动了关于词汇搜索、词条激活及通达阶段的理论争论。

经典 LDT 的理论价值来自词与非词共享视觉和反应要求、但在既有词汇表征上不同。词相对于合法非词的差异可用于估计词汇知识对识别的贡献，高频词与低频词的差异则反映经验强度、语境分布和词汇证据质量的综合作用。然而，双通路级联模型表明，视觉词识别可同时利用整词词汇通路与字形—语音转换通路；可发音伪词尤其增加亚词汇转换需求（Coltheart et al., 2001）。“词汇性效应”由字形、语音、语义和任务决策共同形成，不能视为单一加工器的直接读数。

## 2. 任务逻辑、流程与核心参数

标准单字母串版本通常包含练习和一个或多个正式区组。每个试次先呈现注视标记，继而呈现一个词或非词；参与者以两个按键分别作出“词”和“非词”反应，刺激持续至按键或预设截止时间。研究可在错误后提供反馈，也可仅记录结果并进入试次间隔。典型因变量包括正确反应时的均值或中位数、正确率、遗漏率，以及完整反应时分布。词汇性对比一般为词与非词之差；词频效应则比较低频词与高频词，常表现为低频词反应更慢、错误更多（Forster & Chambers, 1973; Ratcliff et al., 2004）。

不同对比对应不同的可识别问题。真实词与正字法合法伪词的比较强调既有词汇表征与亚词汇分析的差异；高频词与低频词的比较在词汇性保持恒定时估计经验相关优势；相关启动词与无关启动词的比较则考察先行语义信息对目标判断的促进（Meyer & Schvaneveldt, 1971）。三类效应不能互相替代。若研究关注词条可用性，应优先控制非词似词性与语义属性；若关注决策过程，则需操控词/非词先验比例或反应强调，并联合分析正确与错误反应。固定时序便于 ERP 和 fMRI 事件建模，但过短截止时间会增加遗漏和速度—准确性权衡，过长窗口则可能容许额外检查策略。

刺激控制决定上述对比能否获得明确解释。词条件之间至少应匹配长度、字形邻近性、拼写—语音一致性、词类和语义属性；频率估计还依赖语料库及频率函数。词频与语境多样性高度相关，二者对词汇判断时间的解释不能在未经建模时相互替代（Adelman & Brown, 2008）。非词也不是中性基线：随机辅音串、正字法合法伪词和由真实词变换得到的伪词具有不同的“似词性”，会改变拒绝难度、反应标准及词—非词速度关系。词与非词比例、按键映射、速度—准确性指导语及反应截止时间同样可移动决策标准。

扩散模型为分离这些成分提供了可检验的描述。模型以漂移率表示证据积累质量，以边界间距表示谨慎程度，并以非决策时间概括编码和运动成分。Ratcliff 等（2004）发现，词频、非词类型和项目比例对漂移率及决策设置产生可区分影响；只比较平均正确反应时会遗漏错误率和分布形态所包含的信息。该结果也说明，LDT 的条件效应可以来自词汇证据质量变化，也可来自参与者针对刺激集合调整标准。反馈与连续重复会进一步引入学习。对英国词汇项目逐试次建模的研究显示，允许每个试次更新形式—意义映射的模型更好地解释多数参与者的反应时间，提示无显式启动的实验序列亦可能改变后续加工（Heitmeier et al., 2023）。

## 3. 主要行为与神经科学发现

### 3.1 词汇性、词频与决策成分

词频效应是 LDT 中较稳定的群体效应，但其构念含义受项目与任务组成限制。Balota 和 Chumbley（1984）指出，词频不仅影响词汇表征的激活，也会影响词/非词验证与决策阶段，因而不能将全部频率差归于通达速度。大规模项目改变了对此问题的研究方式。英语词汇项目为四万余个词和配对非词提供了跨参与者的词汇判断及命名数据（Balota et al., 2007）；英国词汇项目采用重复测量设计收集 28,730 个英语词及同量非词的数据，使研究者能够同时估计项目属性、个体差异和练习效应（Keuleers et al., 2012）。这些数据库支持连续变量建模，也表明长度、邻近性、语义丰富度和参与者词汇知识均可能与频率效应共变。

近期研究进一步限制了“固定词频效应”的解释。韩语大规模在线 LDT 显示，从青年到老年，反应时间随年龄增长而延长，而正确率和词汇知识相关指标呈现不同变化；高频词优势跨年龄存在，但年龄不能仅由一般加工减慢解释（Baek et al., 2024）。在韩语母语者的英语第二语言研究中，独立 LDT 得到的词汇加工效率比完形测验更能解释英语高、低频词判断差异，说明词频效应也取决于第二语言经验和词汇质量（Baek et al., 2023）。这些发现支持 LDT 对词汇经验差异的敏感性，但跨年龄、跨语言比较必须匹配词汇量、熟练度及频率语料。

### 3.2 EEG 与 fMRI 所揭示的加工阶段

事件相关电位（event-related potential, ERP）提供了区分视觉、正字法和较晚词汇—语义过程的时间信息。Hauk 等（2006）在视觉 LDT 中对单项目连续属性进行回归，发现词长、字母组合频率、词频和形态语义一致性的效应在刺激后数百毫秒内以部分重叠的时间进程出现；这不支持将一次按键前的加工划分为完全串行且彼此隔离的阶段。采用隐藏半马尔可夫多变量模式分析的近期 EEG 研究则发现，高低频词、伪词和随机非词的大部分加工阶段相同，主要条件差集中于靠后的一个决策阶段（Berberyan et al., 2021）。两类结果共同表明，早期词形信息与后期分类证据均会影响最终反应时，头皮电位的时间差不能单独确定其皮层来源。

功能磁共振成像（functional magnetic resonance imaging, fMRI）结果显示，词与匹配非词的比较涉及左侧腹侧枕颞、额下回及颞—顶语义/语音网络，但活动方向随刺激和任务要求而改变。Binder 等（2003）在强调准确性的事件相关 LDT 中发现，真实词识别更多涉及语义相关区域，而非词增加了与字形—语音映射相关的额下区域活动。神经影像元分析进一步表明，同一词—伪词对比在词汇判断与命名任务中形成不同分布：LDT 更强调语义和分类要求，命名则提高语音—发音需求（McNorgan et al., 2015）。fMRI 因而能够描述任务相关网络的空间参与，却不能凭条件相关的 BOLD 差异证明某一区域专门执行词汇通达。近期计算模型将左侧腹侧枕颞活动解释为对“有意义词形/无意义输入”的分级分类，并能同时预测行为与成像数据，但该解释仍与熟悉度、预测误差等理论竞争（Gagl et al., 2022）。

## 4. 范式发展与主要应用

LDT 已由小型因素实验扩展为大型词汇数据库、在线众包、计算建模以及发展和临床研究。大型数据库提高了连续项目属性估计的精度，并允许在同一项目集合内比较参与者差异；在线实施则扩大年龄和语言覆盖范围，但设备、显示器、键盘和网络环境增加了反应时噪声。连续证据模型与逐试次学习模型把正确率、反应时分布和实验序列纳入统一分析，避免将多个过程压缩为一个均值差（Ratcliff et al., 2004; Heitmeier et al., 2023）。

在阅读障碍研究中，词、伪词及其 ERP 差异可用于定位视觉、正字法和语义加工出现分化的时间。成人发展性阅读障碍研究报告了行为成绩以及 P100、N170、N400 和 P600 等成分上的群体差异，但样本规模、正字法透明度和补偿经验限制了推广（Silva et al., 2022）。此类群体差异有助于提出加工假设，不能单独作为个体诊断指标。第二语言和老化研究同理：LDT 可揭示词汇经验与加工效率的关联，若未控制语言暴露、教育、词汇量和一般运动速度，则不宜把条件差直接归因于词汇系统受损。

## 5. 测量效度与解释边界

LDT 对词汇性和词频操控具有良好的实验敏感性，大型数据库也显示项目平均表现可跨样本复现。然而，稳健的群体均值差不保证个体差异分数可靠。扩散模型参数在试次数充分时可获得较好的重测信度，且漂移率与边界间距的重测相关可超过 .70；参数信度会随试次数和估计方法变化（Lerche & Voss, 2017）。短版本更适合估计条件中位数和群体效应，通常不足以稳定拟合个体反应时分布的全部参数。

构念效度的主要限制来自决策污染。按键反应包含编码、验证、标准设置和运动时间，词频与词汇性差异还受速度—准确性权衡影响。错误试次排除规则、反应时截断、按参与者或按项目聚合会改变效应量。可发音伪词越接近真实词，拒绝过程越困难；由真实词系统变换生成的伪词还可能保留特定字形线索。研究设计应预注册刺激匹配、剔除标准和主要对比，并同时报告正确率、反应时分布或适当的层级模型。由单次实验观察到的群体差异只能支持与词汇加工相关的解释，不能据此确定单一认知阶段、神经因果关系或临床分类。

生态效度也需与内部效度分开判断。孤立字母串消除了句法和篇章预测，有利于控制项目属性，却与自然阅读中的连续眼动、上下文约束和阅读目标不同。实验中的词频优势可以说明既往语言经验与当前分类表现相关，不能直接推断同一项目在句子阅读中的注视时间或理解贡献。跨研究复现时还应报告母语、英语熟练度、键盘经验和显示方式；这些变量对总体速度的影响可能大于目标条件差，却未必以相同比例改变条件内效应。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
|---|---|---|---|
| 完整行为实验源码 | T000062 | PsychoPy/PsyFlow 本地行为采集 | https://github.com/TaskBeacon/T000062-lexical-decision-task |
| 浏览器伴随版源码 | H000062 | 与 T 版条件和时序对齐的网页行为实施 | https://github.com/TaskBeacon/H000062-lexical-decision-task |
| 在线运行入口 | H000062 | 浏览器体验与行为数据采集入口 | https://taskbeacon.github.io/psyflow-web/?task=H000062-lexical-decision-task |

T000062 为中文指导语、英文刺激的视觉单字母串 LDT，采集类型为行为。H000062 保留相同刺激池、区组构成、时序和 F/J 映射，但浏览器设备环境与本地 PsychoPy 环境不同；高精度反应时研究仍应评估各自硬件与浏览器时序特性。

### 6.2 实现流程与关键参数

| 层级 | TaskBeacon 当前版本 |
|---|---|
| 练习与正式任务 | 30 次练习；4 个正式区组，每区组 30 次，共 120 次正式试次 |
| 条件组成 | 高频词 30、低频词 30、伪词 60；每区组 15 词与 15 伪词，高/低频词按 8/7 与 7/8 交替 |
| 单试次时序 | 注视 500 ms；字母串至反应或最长 2000 ms；错误按键后反馈 750 ms；空屏间隔 150 ms |
| 反应与计分 | F=词，J=非词；记录正确、错误、超时及反应时；汇总正确率、词/非词正确率和低频减高频的正确反应中位数差 |
| 刺激与调整 | 大写等宽字体；伪词由留出供体替换全部元音形成；正式项目不重复；任务非自适应 |

![TaskBeacon 词汇判断任务流程](../task_flow.png)

**图 1. TaskBeacon 当前版本的试次与区组流程。** 指导语和 30 次练习后进入四个正式区组；每个正式区组含 15 个英语词和 15 个伪词，词项目在高频与低频条件间按相邻区组 8/7、7/8 交替分配。单次试次依次为中央注视点 500 ms、中央大写字母串最长 2000 ms、仅在错误按键后出现红色错误反馈 750 ms，以及空屏试次间隔 150 ms。参与者按 F 判断“词”、按 J 判断“非词”；正确按键和反应时被记录，错误按键触发反馈，未在窗口内反应记为超时。正式项目各呈现一次，伪词供体不作为正式刺激出现；该实现不依据表现调整难度或截止时间。

该实现主要支持词汇性、高低词频正确率与正确反应时比较。其 120 次正式试次显著少于 Ratcliff 等（2004）用于精细分布拟合的大量试次，适宜将低频减高频的中位反应时作为预先指定的行为指标；若拟合个体扩散参数，需另行论证试次数与参数可恢复性。错误反馈和固定 2000 ms 截止时间也会影响决策策略，跨实现比较时应将其作为方法差异报告。

## 参考文献

Adelman, J. S., & Brown, G. D. A. (2008). Modeling lexical decision: The form of frequency and diversity effects. *Psychological Review, 115*(1), 214–229. https://doi.org/10.1037/0033-295X.115.1.214

Baek, H., Gordon, P. C., & Choi, W. (2024). Effects of age and word frequency on Korean visual word recognition: Evidence from a web-based large-scale lexical-decision task. *Psychology and Aging, 39*(3), 231–244. https://doi.org/10.1037/pag0000793

Baek, H., Lee, Y., & Choi, W. (2023). Proficiency versus lexical processing efficiency as a measure of L2 lexical quality: Individual differences in word-frequency effects in L2 visual word recognition. *Memory & Cognition, 51*(8), 1858–1869. https://doi.org/10.3758/s13421-023-01436-0

Balota, D. A., & Chumbley, J. I. (1984). Are lexical decisions a good measure of lexical access? The role of word frequency in the neglected decision stage. *Journal of Experimental Psychology: Human Perception and Performance, 10*(3), 340–357. https://doi.org/10.1037/0096-1523.10.3.340

Balota, D. A., Yap, M. J., Cortese, M. J., Hutchison, K. A., Kessler, B., Loftis, B., Neely, J. H., Nelson, D. L., Simpson, G. B., & Treiman, R. (2007). The English Lexicon Project. *Behavior Research Methods, 39*(3), 445–459. https://doi.org/10.3758/BF03193014

Berberyan, H. S., van Rijn, H., & Borst, J. P. (2021). Discovering the brain stages of lexical decision: Behavioral effects originate from a single neural decision process. *Brain and Cognition, 153*, 105786. https://doi.org/10.1016/j.bandc.2021.105786

Binder, J. R., McKiernan, K. A., Parsons, M. E., Westbury, C. F., Possing, E. T., Kaufman, J. N., & Buchanan, L. (2003). Neural correlates of lexical access during visual word recognition. *Journal of Cognitive Neuroscience, 15*(3), 372–393. https://doi.org/10.1162/089892903321593108

Coltheart, M., Rastle, K., Perry, C., Langdon, R., & Ziegler, J. (2001). DRC: A dual route cascaded model of visual word recognition and reading aloud. *Psychological Review, 108*(1), 204–256. https://doi.org/10.1037/0033-295X.108.1.204

Forster, K. I., & Chambers, S. M. (1973). Lexical access and naming time. *Journal of Verbal Learning and Verbal Behavior, 12*(6), 627–635. https://doi.org/10.1016/S0022-5371(73)80042-8

Gagl, B., Richlan, F., Ludersdorfer, P., Sassenhagen, J., Eisenhauer, S., Gregorova, K., & Fiebach, C. J. (2022). The lexical categorization model: A computational model of left ventral occipito-temporal cortex activation in visual word recognition. *PLOS Computational Biology, 18*(6), e1009995. https://doi.org/10.1371/journal.pcbi.1009995

Hauk, O., Davis, M. H., Ford, M., Pulvermüller, F., & Marslen-Wilson, W. D. (2006). The time course of visual word recognition as revealed by linear regression analysis of ERP data. *NeuroImage, 30*(4), 1383–1400. https://doi.org/10.1016/j.neuroimage.2005.11.048

Heitmeier, M., Chuang, Y.-Y., & Baayen, R. H. (2023). How trial-to-trial learning shapes mappings in the mental lexicon: Modelling lexical decision with linear discriminative learning. *Cognitive Psychology, 146*, 101598. https://doi.org/10.1016/j.cogpsych.2023.101598

Keuleers, E., Lacey, P., Rastle, K., & Brysbaert, M. (2012). The British Lexicon Project: Lexical decision data for 28,730 monosyllabic and disyllabic English words. *Behavior Research Methods, 44*(1), 287–304. https://doi.org/10.3758/s13428-011-0118-4

Lerche, V., & Voss, A. (2017). Retest reliability of the parameters of the Ratcliff diffusion model. *Psychological Research, 81*(3), 629–652. https://doi.org/10.1007/s00426-016-0770-5

McNorgan, C., Chabal, S., O’Young, D., Lukic, S., & Booth, J. R. (2015). Task dependent lexicality effects support interactive models of reading: A meta-analytic neuroimaging review. *Neuropsychologia, 67*, 148–158. https://doi.org/10.1016/j.neuropsychologia.2014.12.014

Meyer, D. E., & Schvaneveldt, R. W. (1971). Facilitation in recognizing pairs of words: Evidence of a dependence between retrieval operations. *Journal of Experimental Psychology, 90*(2), 227–234. https://doi.org/10.1037/h0031564

Ratcliff, R., Gomez, P., & McKoon, G. (2004). A diffusion model account of the lexical decision task. *Psychological Review, 111*(1), 159–182. https://doi.org/10.1037/0033-295X.111.1.159

Rubenstein, H., Garfield, L., & Millikan, J. A. (1970). Homographic entries in the internal lexicon. *Journal of Verbal Learning and Verbal Behavior, 9*(5), 487–494. https://doi.org/10.1016/S0022-5371(70)80091-3

Silva, P. B., Oliveira, D. G., Cardoso, A. D., Laurence, P. G., Boggio, P. S., & Macedo, E. C. (2022). Event-related potential and lexical decision task in dyslexic adults: Lexical and lateralization effects. *Frontiers in Psychology, 13*, 852219. https://doi.org/10.3389/fpsyg.2022.852219
