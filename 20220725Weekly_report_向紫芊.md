# 20220725_Weekly report

+ [1.论文阅读笔记](论文阅读笔记)
+ [2.文献调研](文献调研)
+ [3.工具调研](工具调研)

## 论文阅读笔记

### **Beyond subjective judgments: Predicting evaluations of creative writing from computational linguistic features**
#### **研究背景**
 * 传统的创造力评估方法：
   * 发散思维测验（Alternate uses task (AUT)）
   * 远距离联想测验（Compound remote associates (CRA) problems）
   * 创造力自我报告（Creative Behavior Inventory (CBI) short form）
 * 创造力写作的评估方法目前主要是人为评估，基于打分者的经验对于文章的创造力进行评估，是比较主观的。
 *  **An analytical rubric for assessing creativity in creative writing**这篇文章介绍了创造力写作的一些客观评分标准（具体可见7月11日的周报），即：
   * **Image**：想象是创造性写作的核心，这样的描写包括声音、气味、感受、情绪等等，优秀的作者能够以很好的诱导读者，用文字将读者导入到故事之中。**充满想象的文章避免概括、抽象、平面写作等元素，而是使用丰富而具体的事件描述来替代**。
   * **Voice**：评估作者自己**写作风格的独特程度**，可以通过多种方式，包括独特和特殊的选择词（例如，罕见的、老式的或俚语词，在故事的特定背景下不典型，或自创词语或表达)，使用有趣或复杂的句子结构和标点符号、隐喻的使用和其他比喻，或通过叙述者的独特视角或态度。
   * **Originality**：评估故事的**原创性**程度。
#### **问题提出（本篇论文的切入点，研究问题）**
 * 基于目前已有的创造力写作评估标准，即Image、Voive以及Originality，制定对应的文章语法特征。
 * 使用语法分析工具Coh-Metric以及LIWC分析创造力文本的句法特征。
 * 分析人为评分的Image、Voive以及Originality、使用传统创造力评价方法（AUT、CRA、CBI），以及使用计算机评分(基于Coh-Metric和LIWC)的相关性。
 * 探索创造力写作的自动化评分，从主观到客观。
#### **研究设计（实验设计、数据获取等）**
 * **实验程序**
   * 招募被试；
   * 被试完成AUT、CRA、CBI；
   * 被试完成创造力写作；
   * 人为对被试文章的Image、Voive以及Originality进行打分；
   * 基于Coh-Metric和LIWC评分；
 * **从创造力写作评估标准Image、Voive以及Originality到语法特征的映射**
   * **Coh-Metrix indices**
     * **Narrativity**:反映了文本与叙事体裁的契合程度
     * **Deep cohesion**:文本的结构与连接词紧密联系在一起，表示因果关系或意向性
     * **Referential cohesion**:体现内容词和想法之间的联系程度
     * **Syntactic simplicity**:文本中的句法结构的简单程度
     * **Word concreteness**:根据文本中的词唤起比抽象词更容易处理的具体心理意象的程度来计算。
   * **LIWC dimensions**
     * **基于Image**
        * **Insight**:这个类别包含单词,比如think,know,consider等用来描述思想、感受和心理状态的词语。
        * **See**:包含诸如view、saw之类的词，它们可以描述视觉。
        * **Hear**：包含listen和hearing描述声音体验的词语。
        * **Feel**：包含feels、touch等可以描述感觉和身体感觉的词语。
        * **Body**:包含cheek或hands,可用于描述感觉和身体感觉。
     * **基于Voice**
        * **Informal language**:这一类包括非正式语言，例如脏话、网络用语等等。
        * **Dictionary words**：这是文本包含的 LIWC 词典中的单词个数。选择了这个变量，因为广泛而多样的单词用法可能有助于创造独特的语言表达。
        * **Number of words per sentence**：每个句子的字数。
        * **Punctuation**：标点。
        * **Use of commas specifically**：逗号的使用。
        * **Authenticity**：衡量语言的真实性程度。真实性得分高的文章中中包含许多第一人称词和现在时。
动词等特征。
     * **基于Originality**
        * 原创性分数反映了一个故事的想法或情节是否原创。 因此，与 Image 和Voice相比，原创性在很大程度上是根据上下文定义的（即，原创相对于其他故事），因此很难关联文本中固有的特定语言特征。
#### **实验结果**
  * 在study1中，Image和Voice与几乎所有其他创造力测量相关（唯一的例外是Image和 AUT之间的不显著相关性），而原创性Originality未能与其他创造力测量一致地相关。 在更广泛的学生样本 (Study2) 中，Image、Voice和Originality与创造力任务的表现表现出一致的相关性。
  * 在**Coh-Metric**计算结果中，**Referential cohesion**成为两项研究最一致的的预测因子，显著预测两者Image和Voice。
  * 在**LIWC**计算结果中，Image被类别Insight一致且负面地预测，Feel类别中的词对它进行了积极预测，并且在研究 1 中也显示出与Body相关词的显着关联。与预测相反，与Hear和See相关的词并不能预测Image分数。
  * 在**LIWC**计算结果中，Vioce始终被归类为真实Authenticity的语言积极预测，而 LIWC 词典中的单词数量为负面预测（即，更少的词典单词对应于更高的Vioce分数）。还发现标点符号和Voice分数之间的关联在研究 1 中显著。非正式单词Informal language仅在研究 1 中预测Voice分数，而逗号仅在研究 2 中预测。每个句子的单词数不能预测Voice分数。
#### **总结与思考**
  * 本篇论文的目标是探索是否可以通过**计算机语言分析预测人类对创造力的评分**。
  * 指标Image、Vioce、Originality具有可靠的信度和效度。
  * 本文的创新点是**建立指标Image、Vioce、Originality和文本的语言特征的联系**，并使用文本分析工具 Coh-Metrix 和 LIWC 对文本进行分析。
  * 本研究结果表明，借助量规（Image、Vioce、Originality）对创造力进行的人类评分可以在某种程度上从客观测量的文本语言特征中预测出来。 这些结果将评估标准确立为评估创意写作的有用工具，并说明，**创意写作的某些方面可以通过计算机化测量来捕捉**——这些证据值得在后续研究中应给予更多关注。

## **文献调研（关注作者历史发表内容）**

* **Amabile T. M.**
 * Amabile T M, Barsade S G, Mueller J S, et al. **Affect and creativity at work**[J]. Administrative science quarterly, 2005, 50(3): 367-403.
 * Amabile T M, Conti R, Coon H, et al. **Assessing the work environment for creativity**[J]. Academy of management journal, 1996, 39(5): 1154-1184.
 * Amabile T M, Collins M A, Conti R, et al. **Creativity in context: Update to the social psychology of creativity**[M]. Routledge, 2018.
 * Amabile T M. **The social psychology of creativity: A componential conceptualization**[J]. Journal of personality and social psychology, 1983, 45(2): 357.
 * Amabile T M, Pratt M G. **The dynamic componential model of creativity and innovation in organizations: Making progress, making meaning**[J]. Research in organizational behavior, 2016, 36: 157-183.
 * Amabile T M. **Social psychology of creativity: A consensual assessment technique**[J]. Journal of personality and social psychology, 1982, 43(5).
* **Crossley S. A.**
 * Crossley S A. **Linguistic features in writing quality and development: An overview**[J]. Journal of Writing Research, 2020, 11(3): 415-443.
 * Crossley S A, McNamara D S.** Understanding expert ratings of essay quality: Coh-Metrix analyses of first and second language writing**[J]. International Journal of Continuing Engineering Education and Life Long Learning, 2011, 21(2-3): 170-191.
 * McNamara D S, Crossley S A, McCarthy P M. **Linguistic features of writing qualit**y[J]. Written communication, 2010, 27(1): 57-86.
 * Crossley S A, Louwerse M M, McCarthy P M, et al. **A linguistic analysis of simplified and authentic texts**[J]. The Modern Language Journal, 2007, 91(1): 15-30.
 * Crossley S A, Greenfield J, McNamara D S. **Assessing text readability using cognitively based indices**[J]. Tesol Quarterly, 2008, 42(3): 475-493.
 * Crossley S A, Allen D B, McNamara D S.** Text readability and intuitive simplification: A comparison of readability formulas**[J]. Reading in a foreign language, 2011, 23(1): 84-101.

## **工具调研**
*  **Coh-Metric**
  * Coh-Metrix 通过分析文本的多个层次级别来自动测量**连贯性**和**可读性**。超越了文本的表面特征，进入了因果、时间和意图的凝聚力。衔接反映了构建情境模型（即整体心理表征）的文本特征。这些特征的范围从单词到短语再到构建连贯文本表示的句子。 Coh-Metrix 产生的指标是通过潜在语义分析 (LSA)、句法解析器和传统难度指数（如单词和句子长度）的组合得出的。
* **LIWC**
  * LIWC 是一种流行的文本分析工具，它独特地评估心理上有意义的类别，例如情感内容或社会关系。 LIWC 通过给定文本与一组 80 个预定义字典（例如，积极情绪字典中的示例 ：happy）比较分析每个单词，然后计算文本中属于每个类别的单词的百分比。 目前已发现 LIWC 可以成功预测心理相关结果，包括欺骗（Newman et al., 2003），学生的成绩（Robinson、Navea 和 Ickes，2013 年）和大学学业成功（Pennebaker 等人，2014 年）。
