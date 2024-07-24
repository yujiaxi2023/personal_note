# **Benchmarking Attention Mechanisms and Consistency Constraint Semi-Supervised Learning for Post-Flood Building Damage Assessment**

先验是我们获得benchmark的重要指导条件

Abstract:

Keywords: Flood disaster, Attention mechanisms, Semi-supervised learning, benchmark, Consistency constraint, Prior knowledge

###       **I.**            **INTRODUCTION**

Paragraph 1: 描述研究洪水后抢险救灾的大背景，研究的动机和主要的挑战，针对数据集的变化进行说明

Paragraph x:

根据洪水灾害的特征，有数据集的特征，图像的特征，然后我们认为注意力机制和半监督学习是很好解决这些特征问题的关键

在本章节要强调，研究洪水或者专一灾害特征的深度学习benchmark的研究非常稀少，要指出过去的工作运用模型的本质是初级粗糙的，所以我们需要引入到现在CD模型中使用的更复杂的处理技巧，用来明确应用于该任务的Benchmark或者是baseline到底是什么（benchmark是较好的基准，baseline是最低限度的基准）

在这些处理技巧中我们根据问题的特征认为，注意力机制和半监督学习是很好的解决办法

在半监督学习和注意力机制中，我们选择了先验作为指导，因为是针对具体问题，我们认为先验因素是有价值的，我们认为在图像中关注的点应该消除无效的背景影响，所以在先验注意力机制中使用了视觉神经的关注一点，抑制周边神经元特性的模块，这种是模型框架的改进，是针对图像的。在半监督学习方法中，认为我们要考虑到对无标签数据分布的预测，这一点需要跟数据集的类别分布做结合，我们认为是类别分布导致了洪水任务的特殊性，然后所以要对类别分布进行改进，我们要进行实验，看哪种类别分布更接近于真实分布，然后用该方法去指导运用什么一致性正则化方法的具体应用，这种是针对数据集分布和数据集不足的改进。我们认为认识图像，需要改进模型，认识数据集，需要改进学习方法。

所以对于洪水任务，我们采用了先验的知识去针对性的改进，获得benchmark方法。为什么获得的是benchmark方法，是因为顶刊中没有这种的sota方法，所以对比对象缺少。

贡献是：

（1）    对于认识细微图像，我们用了简单的先验注意力模块改进，在全监督上达到了很好的效果

（2）    对于数据不足和不平衡，我们使用的伪标签一致性正则化方法，获得了在某些比例的半监督数据集中最佳的表现

（3）    对于抢险任务，我们的改进模型框架可以更好的比这些CD模型更适应抢险场景，因为Recall提升了很多，并且我们分析了多标签场景下的一些模型表现，可以指导后续的在xview数据集上的改进工作

在传统的利用遥感图像进行变化检测的研究中，灾害评估是一项重要的下游任务 [1]，而在基于深度学习的灾害评估研究领域的研究者，并没有很重视模型架构的设计。所以本文希望引入CD中的复杂框架来确定洪水灾害评估任务中的benchmark模型表现。

###    **II.**            **RELATED WORK**

#### A.   Disaster Assessment and Change Detection

常规的变化检测任务一般都是二分类的semantic segmentation，而灾害评估任务可以看作其多分类延伸，早期的Nguyen等人[2]使用预训练的VGG-16模型首次分析了社交媒体平台上发布的灾害场景图片，证明了深度学习模型在灾害评估领域的应用潜力，为了开发特定用于灾害场景的深度学习模型，Gupta等人[3]创建了xBD数据集，基于这个数据集Gupta等人[4]创建了RescueNet，该模型使用ResNet50作为特征提取器，并微调特征解码过程来增强模型提取受损建筑物的能力。首先是fully convolution network（FCN）在变化检测领域（单流 [5] 和双流模式 [6]）的成功应用，Zheng等人在灾害评估领域也同样采用了Siamese架构并使用FCN作为decoder建立他们的模型[7]。U-Net [8] 因为其特有的skip connection能够消除下采样过程中的信息丢失备受CD研究者的欢迎，Papadomanolaki等人[9]基于U-Net结构使用了结合LSTM模块的Recurrent neural networks处理时间相关数据，Fang等人[10]使用U-Net++变体并采用试图尽可能的保留更多的浅层信息。而后注意力机制的引入扩大了CD模型的感受野，使模型获取全局信息的能力变强 [11][12]。同时在灾害评估领域也有一些工作采用了类似的结构，Wu等人[13]使用U-Net和Attention 模块在xBD数据集上评估建筑物损坏，Xing等人[14]则是添加self-attention module利用多模态数据评估建筑物洪水脆弱性。而在最新的CD模型进展中，模型开始关注于利用注意力机制的深层特征融合[15]，利用生成模型和视频处理的手段添加时间维度信息[16]，通用的MetaChanger架构来研究深层信息的aggregation-distribution和feature exchange等交互策略[17]等等。

通过比较CD和灾害评估领域的先端的模型架构研究的进展，发现灾害评估领域的研究更愿意使用在CD中已经被证明行之有效的benchmark方法，例如全卷积网络 [7]，双流结构 [18]，U-Net结构中的skip-connection，attention mechanism [13][14]等。因此本文会基于这些基础框架，针对洪水事件这种在卫星图像以及数据结构中都展现了特殊性的任务，我们的直觉利用先验知识从注意力机制和半监督学习策略两个角度建立新的benchmark方法将会比只利用物体自身的特征信息的方法更加合适。

#### B.    Attention Mechanism

注意力机制在计算机视觉领域的应用主要是用于捕捉图像上的respective field。原理是基于图像的通道维度[19]和空间维度[20]，通过加权的方式，模型将对图像的不同区域产生注意力。

在经典工作Transformer中，自注意力是其提高模型感受野范围的重要模块 [21]，在遥感领域中，BIT [12/22] 融入了attention在natural language processing (NLP) 领域的理解，也就是将信息视为token进行定位，利用卷积神经网络对输入图像embedding后使用Transformer模块检测。Xing等人 [23]在U-Net中添加了自注意力来评估建筑物的洪水脆弱性。Fang等人 [24] 将输入的变化前后图像embedding为4组特征图，并认为需要设计通道选择策略，因此采用了channel attention module让模型更关注通道信息。Chen等人 [25] 设计了一种pyramid spatial–temporal attention module (PAM) 用于利用获取的空间信息。Zhang等人 [15/26] 使用了空间和通道注意力作为深度监督信息的一部分添加到网络中。

在变化检测中，很多研究采用了单维度（channel 或者 spatial attention）可学习的自注意力模块来进行注意力的改进，但是在具体问题的时候，本文认为应采取不同的attention策略，例如洪水信息这种数据量较少，包含信息不多的，采用low-rank attention with prior可以降低自注意力的复杂度，同时更能针对问题特征创造客制化模块。

利用先验创造注意力模块有很大的灵活性。例如Hou等人[27]使用Interaction-Aggregation-Update（IAU）模块包含全局的空间，时间和channel context information，用于行人识别任务。Zhang等人 [28] proposed an effective Relation-Aware Global Attention（RGA）module，用于捕获全局的空间和channel结构信息用于注意力学习。Yang 等人 [29] 依据神经元的活动方式建立了一个能量函数，让模型可以遵循神经元的空间抑制性特征来处理图像所有维度的信息。本文根据洪水事件对建筑物破坏特征是微小的这一特点，我们采用了一种利用神经元接收视觉刺激后的放电机制作用特点的无参注意力模块 [29] 对CD模型进行改进。

#### C.    Semi-supervised Learning

Semi-supervised Learning (SSL) 是一种通用的克服标记数据不足的深度学习方法，SSL采用未标记数据 $D_u$ 和标记数据 $D_l$ 组成的数据集对模型进行训练，通常情况下如果采用同样的模型策略去应对无标签数据会导致模型分类性能降低 [30] 。因此需要设计利用 $D_u$ 的算法，Consistency constraint是一种重要的半监督学习方法，它假设在相同输入条件下，神经网络中的随机性（e.g. Dropout or Data Augmentation）不会改变模型的预测输出 [30] ，2016年后研究者们开始如何在样本中添加随机性实现一致性正则化，Sajjadi et al. [31] 提出了一种无监督损失，它通过对同一数据点进行两次随机变换，然后通过最小化两个变换后的数据点经过网络后的差异来进行学习。Miyato 等人 [32] 创建了Virtual Adversarial Training (VAT)将其生成的带噪声样本替换为模型预测输出。Verma等人 [33] 通过插值的增加更多的数据点用于数据集增强，通过训练让模型预测值和对应的插值保持一致。

Proxy-label method是将模型预测的伪标签分配给无标签样本，通过最小化无标签数据的类别概率条件熵，使得类别在低密度间分离 [34] ，其代表性工作是label propagation [35] 和自训练 [36] ，Iscen et al. [35] 基于特征嵌入来构建样本间的相似性图。然后将伪标签从已知样本传播到无标签样本，利用相似度分数决定传播权重。自训练中需要在有标签数据上构建分类器，并使用分类器预测无标签数据，将置信度最高的数据转换为标签样本呢，Xie等人 [36] 运用了这一思想在深度学习中，取得了显著的效果。

Proxy-label + Consistency constraint method是一种结合方法。Berthelot et al. [37] 首次创建将一致性正则化和熵最小化作为整体性措施的半监督学习方法，而后引入了distribution alignment 和 augmentation anchoring的方法鼓励边际分布接近真实标签分布，并让模型预测保持在网络容差范围内增强进行采样 [38] ，但是该工作只关注了真实标签类别分布。Sohn等人 [39] 沿袭着学习伪标签的预测分布范围，制定了将无标签数据进行强弱增强处理的手段建立了FixMatch，Yang等人 [40] 在此基础上，通过约束强扰动和弱扰动的一致性建立的UniMatch，这些研究是研究如何对图像进行预处理生成不同的增强版本的图像作为一致性正则化干扰。

本文认为因为灾害事件的特征导致数据集不足和不平衡的特点，采用proxy-label和consistency constraint的综合方法是有益的，我们认为其中关键在于训练将伪标签分布接近无标签数据的真实标签数据分布，因而根据先验知识假设了4种不同的image-level参考分布作为扰动用于规范生成的伪标签。

### **III.**            **PROPOSED METHOD**

#### A.   Overview of Proposed Method

![[Pasted image 20240618195003.png]]
Fig. 1. The overview of the proposed method（图字太小，右边informatics，画面范围不匹配）

本文基于先验知识的引入有助于建立针对特定任务的深度学习方法的理解搭建了the prior knowledge-based deep learning approach for post-flood building damage assessment. The overview of the proposed method is illustrated in Fig. 1，它有一个全监督过程和一个半监督过程组成。通过全监督过程测试添加的先验注意力模块是否能让模型对图像中的细微变化捕捉能力产生积极影响。通过半监督过程测试设置的consistency constraint半监督方法能否帮助CD模型从无标签数据中获得有价值的信息。

本文的采取的是两段式的改进：（1）模型架构是决定模型从单张图片中获得信息的关键，因此在关注图像的细微变化和消除庞大的背景噪声这一方面，注意力机制是实验的对象，对CD模型的编码器部分采取了self-attention和基于视觉神经作用机制的prior-attention两种改进措施，通过对浅层信息的重点保留并融合深度信息提升模型的感知能力。

（2）学习策略决定了模型从整个数据集中获取的信息。本文侧重于利用无标签数据的一致性正则化和Entropy minimization的综合方法。一致性正则化的理念是在预测值上施加扰动，以确保不同类别在低密度区域中有足够的分离度。采用image-level的预测标签分布作为现实扰动。本文考虑了4种策略来近似真实标签分布：1）采用充分预训练的模型对无标签数据进行预测生成的伪标签预测组。 2）同一数据集下的真实标签组。  3）采用充分预训练的模型对有标签数据进行预测生成的真实标签预测组。 4）将上述三种策略结合。当预设的参考分布接近真实分布的时候对获得的预测值置信度是最高的。

上述改进将在下面的小节中详细描述。

#### B.    Semi-supervised Learning Framework

![[Pasted image 20240618161656.png]]
Fig. 2. 半监督学习过程

采用consistency constraint 和 proxy-label method的综合半监督学习方法框架如Fig. 2所示，本实验中的半监督数据集$D\sim{D_l\cup{D_u}}$ , 可以看作两个部分：标签数据集$D_l=\{(x_{l\_\,pre}^{\mathcal{i}}\;,\;x_{l\_\,post}^{\mathcal{i}})\;,\; y_l\}_{\mathcal{i=1}}^{M} \quad y_l\in\{0,1,2,3\}^L$ , 和无标签数据集$D_u=\{(x_{u\_\,pre}^{\mathcal{i}}\;,\;x_{u\_\,post}^{\mathcal{i}}) \}_{\mathcal{i=1}}^{N}$ , 其中$(x_{u\_\,pre}\;,\;x_{u\_\,post})$ 和 $(x_{l\_\,pre}\;,\;x_{l\_\,post})$表示灾害前后的图像对,$M$和$N$表示图像对的数量，$y_l$是长度为$L$的向量，每个元素都取自集合$\{0,1,2,3\}$，代表4种可能的类别。

首先使用$D_l$在变化检测模型$f_\theta$上充分训练获得预训练的变化检测模型$f_{\theta}^{’}$，在将标记图像$x_l$输入到预训练模型$f_{\theta}^{’}$后，可以获得segmentation predictions $\hat{y}_l$, 利用$\hat{y}_l$和ground truth $y_l$就可以通过监督损失$\mathcal{L}_s$对模型进行优化。对无标签数据集$D_u$，本文将采用proxy-label和consistency training的综合方法进行训练，其中proxy-label method的本质是通过熵最小化让模型在低密度分 [34]，预训练模型$f_{\theta}^{’}$会通过输入无标签数据$x_u$生成预测值$\hat{y}_u$，通过计算并最小化$\hat{y}_u$的信息熵$\mathcal{L_{u\_\,entropy}}$优化模型。

![[Pasted image 20240617202837.png]]
Fig. 3. 获得reference distribution

本研究的重点在设计不同的realistic perturbation进行consistency training，采取下面四种假设生成参考分布，当参考分布更接近真实标签分布时添加的干扰是最有积极影响的：

1）采用充分预训练的模型对无标签数据进行预测生成的伪标签预测组，该假说认为如果模型足够可靠，那生成的伪标签会更接近符合现实分布的。

2）同一数据集下的真实标签组，该假说认为无标签数据跟有标签数据同属于同一个事件或者同类事件，那标签分布应该是符合相同规律的。

3）采用充分预训练的模型对有标签数据进行预测生成的真实标签预测组，该规则是建立在上述两种假说的基础上设立，因为预训练模型一定会产生错误分类噪声，而使用方法2) 完全真实标签并不会包含模型产生的噪声干扰，所以通过真实标签的预测值与前两种策略对比，判断是让预测分布更多学习真实分布有益还是更多学习错误分布有益。

4）使用伪标签预测组，真实标签组和真实标签组预测组分别作为参考分布与预测概率分布求相似度，然后将计算的损失函数用相同权重加和，该策略是为了印证1）2）3）策略中的正负面影响关系。

如Fig. 1的所示，通过control unit按照采取的策略不同控制输入的标签组生成不同的参考分布$Q$，并将无标签数据产生的预测$\hat{y}_u$ 转化为类别分布$P$，利用$P$和$Q$计算kl散度$\mathcal{L_{u\_ \,kl\,divergence}}$对模型实施优化。

生成参考分布$Q$的过程如Fig. 3所示，以batch为单位，将生成的标签组统计各分类下的元素数量储存到distribution buffer中，同时设置一个$buffer\ size = n$，当buffer中统计了一定数量的标签后计算平均值获得reference distribution $Q$。

综上，模型的整体损失定义如下：

$$  \mathcal{L = L_s + \alpha L_{u\underline{~}entropy} + \beta L_{u\underline{~}kl\,divergency}}  $$

通过$\alpha$, $\beta$来控制不同semi-supervised loss的重要程度，在pre-trained模型的基础上在semi-supervised数据集上进行训练获得最终的模型。

#### C.    Self-attention CD Network

在CD领域已经有一些研究采用了self-attention机制，例如Xing等人[14]在多模态分支之间添加自注意力生成特征的FSA-UNet，Chen等人 [25] 设计的一种pyramid spatial–temporal attention module (PAM) 用于利用获取的空间信息的STANet，Zhang等人[15]对深度信息进行注意力增强的DSIFN, Chen等人[12]利用Transformer encoder和decoder设计的BIT。

在其中BIT是本研究主要参考的设计，网络将输入的双时相图片$(x_{pre}\;,\;x_{post}) \in \mathbb{R}^{H\times{W}\times{C}}$，其中$H$，$W$和$C$代表图像的高，宽和Channel信息，通过第一次卷积变化形成了Feature maps $(F_{pre}, F_{post})$，这一操作的目的压缩图像信息减少计算负担，然后将Feature maps再进行point-wise convolution to obtain tokenizer $(T_{pre}, T_{post}) \in \mathbb{R}^{L^{’} \times {C}}$，其中$L^{’}\ll (H \times W)$ 经过上述变化将图像信息转化为了类似NLP中的tokenizer，将$(T_{pre}, T_{post})$concat形成$T \in \mathbb{R}^{2L^{’} \times {C}}$作为Transformer的输入，要进行self-attention计算，需要对$T$进行线性映射为三个输入（query $Q$， key $K$，value $V$），公式如下：

$$  \begin{align} \mathbf{Q} = \mathbf{X}\mathbf{W}_q,  \\ \mathbf{K} = \mathbf{X}\mathbf{W}_k,  \\ \mathbf{V} = \mathbf{X}\mathbf{W}_v,  \end{align}  $$ 

where $\mathbf{W}_q, \mathbf{W}_k, \mathbf{W}_v \in \mathbb{R}^{C \times d}$ are learnable weight matrices. 其中$C$为原tokenizer的channel dimension，$d$为权重矩阵的channel dimension。根据$Q$，$K$，$V$可以计算one self-attention head:

$$  \text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d}}\right)\mathbf{V}  $$

为了避免模型计算速度过慢，以及提高robustness，Transformer采用了multi-head self attention (MSA)，可以看作对multiple independent attention heads 进行concat操作。Formally:

$$  \text{MultiHead}(\mathbf{X}) = \text{Concat}(\text{head}_1, \text{head}_2, \ldots, \text{head}_h)\mathbf{W}_O  $$

where $W_O \in \mathbb{R^{h\times{d}\times{C}}}$是将编码后信息转换回原来$T$的tensor size的linear projection matrices。$h$ is the number of attention heads.

经过Transformer encoder获得编码后的上下文信息$T_{new} \in \mathbb{R}^{2L^{’} \times {C}}$，将$T_{new}$ split into two sets $(T_{new\_\,pre}, T_{new\_\,post})$，然后分别输入到Transformer decoder中，decoder中的query $Q$ 是从Feature maps $(F_{pre}, F_{post})$ 线性变化得到，因此decoder的multihead cross attention (MA) 定义为：

$$  \begin{align} \text{{MA}}(\mathbf{F}_{i}, \mathbf{T}, \mathbf{T}) = \text{{Concat}}(\text{{head}}_{1}, \ldots, \text{{head}}_{h}) \mathbf{W}_{O},\\  \quad where \  \text{{head}}_{j} = \text{{Att}}(\mathbf{F}_{i}\mathbf{W}_{qj}, \mathbf{T}\mathbf{W}_{kj}, \mathbf{T}\mathbf{W}_{vj}) \end{align}  $$

where $\mathbf{W}_{qj}, \mathbf{W}_{kj}, \mathbf{W}_{vj} \in \mathbb{R}^{C \times d}$ , $W_O \in \mathbb{R^{h\times{d}\times{C}}}$ are the linear projection matrices, and $h$ is the number of attention heads.

最后使用卷积层组成的prediction head差分处理attention feature maps获得最终的change maps。

#### D.   Prior-attention CD Network

![[Pasted image 20240618161630.png]]
Fig. 4. Prior-attention CD model architecture

BIT将图像转换为语义密集的token，使用自注意力生成attention feature maps，这种操作可以视为对浅层关键信息的提取和放大，这样使得差分后的特征变化更加明显。

本文在设计prior-attention CD model的时候，考虑到灾害场景下的变化特征微小，容易在下采样过程中丢失，因此采用了能保留浅层信息的UNet作为基础模型添加prior-attention module如Fig. 4所示。在编码阶段，利用5个卷积单元生成下采样的特征图，从而提取多尺度特征，在解码阶段，本文选择在skip connection部分使用attention是因为下采样前的粗尺度信息包含的变化特征更全面，但是不能保留所有的粗尺度特征因为可能会导致背景噪声淹没了微小的变化特征。

_Prior-attention module:_ 本文采用的是Yang等人 [29] 依据神经元的空间抑制属性建立的先验注意力模块，该工作设计了一个能量公式用于计算神经网络中每个神经元的重要性：

$$ e^*_t = \frac{4(\hat{\sigma}^2 + \lambda)}{(t - \hat{\mu})^2 + 2\hat{\sigma}^2 + 2\lambda} $$

Here, $$\mu = \frac{1}{S} \sum_{i=1}^{S} x_i \quad$$ 和 $$ \quad \hat{\sigma}^{2} = \frac{1}{S} \sum_{i=1}^{S}(x_i - \hat{\mu})^2$$ , where $t$ and $x_{\mathcal{i}}$ 是输入特征$X \in \mathbb{R}^{H\times{W}\times{C}}$的一个通道中的目标神经元和其他神经元，$\mathcal{i}$是spatial dimension的index，其中$S=H\times{W}$是一个通道中的神经元数量。$e^*_t$越低，目标神经元$t$和周围神经元的区别越大，就代表越重要。因此每个神经元的重要性可以通过$$ \frac{1} {e_t^{*}} $$获得。

最终的attention maps $\widetilde{X}$ 定义为：

$$ \widetilde{X} = \text{sigmoid}\left(\frac{1}{E}\right) \odot X $$

其中$E$是group了所有spatial和channel维度的$e^*_t$。

将生成的attention map concatenate decoder中的卷积层，最终project回到像素空间获得变化图。

#### E.    Loss Function

我们的proposed method中有两个训练过程，总共使用了3种损失对CD model训练，其中全监督训练过程的损失函数与半监督训练过程中的监督部分的损失函数一致，均为$\mathcal{L_s}$，半监督损失有两部分组成，分别是最小化熵损失和KL散度。

1) Supervised Loss:

本次实验是多分类任务，因此采用weighted cross-entropy loss优化监督学习中的预测概率分布，该loss仅对标记数据作用，可以表示为

$$ \mathcal{L_s} = -\frac{1}{M} \sum_{i=1}^{M} \sum_{c=1}^{4} w_c y_{i,c} \log(p_{i,c}) $$

其中：$\mathcal{L_s}$ 表示损失，$M$ 表示样本数量，$i$ 是样本的索引，$c$ 是类别的索引，这里是 1 到 4，表示四个损伤类别，$w_c$ 表示类别的权重，$y_{i,c}$ 是样本 $i$ 对应类别 $c$ 的真实标签，$p_{i,c}$ 是样本 $i$ 对应类别 $c$ 的模型预测概率分布。

2) Entropy Minimization Loss:

一般而言，模型更容易对无标记数据产生低确定性的高熵预测，伪标签方法是基于假设同类数据在低密度区域的聚类是分离的[36]，所以需要在训练过程中最小化伪标签的信息熵阻止决策边界靠近数据点，本实验采用的信息熵损失项定义为：

$$ \mathcal{L_{u\_\,entropy}} = -\frac{1}{N}\sum_{i=1}^{N} \sum_{c=1}^{4} p_{i,c} \log p_{i,c} $$

其中： $\mathcal{L}$ 表示损失函数,  $N$ 表示样本数量, $c$ 是类别的索引，这里是 1 到 4，表示四个损伤类别,  $p_{ij}$ 是样本 $i$ 属于类别 $c$ 的概率。

3) Kullback-Leibler divergence:

因为没有原始标签，因此我们需要通过假设无标签数据的真实标签分布作为参考分布$Q$，通过学习让预测概率的类别分布$P$接近参考分布，我们使用常见的KL散度用来衡量这两个分布之间的差异，KL散度的定义如下：

$$ D_{KL}(P \| Q) = \sum_{i} P(i) \log\frac{P(i)}{Q(i)} $$

其中 $ P(i) $ 和 $ Q(i) $ 分别表示分布 $ P $ 和 $ Q $ 在第 $ i $ 个元素上的概率。依据KL散度，损失函数如下：

$$ \mathcal{L}_{\text{u\_\,kl\,divergency}} = \frac{1}{N} \sum_{i=1}^{N} D_{KL}(P, Q) $$

其中： $\mathcal{L}_{\text{KL}}$ 表示KL散度的损失函数， $N$ 表示样本数量， $D_{KL}(P,Q)$ 表示标记数据的真实分布和模型预测分布之间的KL散度，$P$ 表示模型预测的分布，$Q$ 表示无标记数据的参考分布

这个损失函数的目标是通过最小化KL散度来使模型的预测分布尽可能接近于标记数据的真实分布，以提高模型对未标记数据的性能。

综上，模型的整体损失定义如下：

$$  \mathcal{L = L_s + \alpha L_{u\underline{~}entropy} + \beta L_{u\underline{~}kl\,divergency}}  $$

通过$\alpha$, $\beta$来控制不同semi-supervised loss的重要程度，在pre-trained模型的基础上在semi-supervised数据集上进行训练获得最终的模型。

### **IV.**            **EXPERIMENT AND RESULT**
#### A.   Description of Dataset

xBD数据集is the largest building damage assessment dataset (Gupta et al., 2019), 图像来源于Maxar/DigitalGlobe开放数据计划（https://www.digitalglobe.com/ecosystem/open-data），数据集包含超过45361平方公里的850736个建筑实例。xBD提供了building polygons，labels of damage levels (Table x) and high spatial resolution (HSR) bitemporal optical satellite images before and after various disaster events with size of 1024 × 1024 pixels and below a 0.8 meter ground sample distance (GSD) mark. 为了评估多种灾害类型中的建筑物损坏，xBD采用联合损坏量表the Joint Damage Scale，，是在the National Aeronautics and Space Administration (NASA), the California Department of Forestry and Fire Protection (CAL FIRE), the Federal Emergency Management Agency (FEMA), and the California Air National Guard [3] 的帮助下创建的。The Joint Damage Scale包括四个离散的损伤级别：No-Damage, Minor Damage, Major Damage, Destroyed, as the damage classification criteria.

本研究中关注于单纯的洪水事件，在xBD数据集中手动选择了分类为洪水的2个灾害事件的相关样本构成我们的数据集, 数据集中包含1064 pairs HSR remote sensing images, 为了便于训练，图像按照 6:2:2的比例分为训练集，验证集和测试集，并裁切为256 × 256像素大小的图像块，在train set上采用128 pixels的stride进行图片裁切，在validation和test set中采用256 pixels的stride进行裁切，最终获得93786/ 10224 / 10224对图像块。本研究使用的数据集和原xBD数据集的差异如Table 1所示。

Table 1. xBD数据集中所有事件和洪水事件的各分类标签比例

|   |   |   |
|---|---|---|
|Included disaster events|All events|Flood events|
|Original sample number|22068|2128|
|No-damage class ratio|87.20%|91.70%|
|Minor-damage class ratio|4.57%|4.28%|
|Major-damage class ratio|5.48%|3.68%|
|Destroyed class ratio|2.74%|0.33%|

#### B.    Implementation Details

本次实验使用了PyTorch框架，使用单张NVIDIA RTX 4090 GPU进行训练。选择（Adam）作为优化器，初始学习率为（3e-5），其中每（60）次迭代初始学习率会衰减（80%），训练epoch数设置为（150），batch size设置为（24）。

在监督学习设置中，先验注意力模块的能量函数偏置项$\lambda$设置为1e-4，the size of convolution kernel is set to 3×3, and the number of kernels in each convolution unit are set to {16, 32, 64, 128, 256} for the basic UNet。

在半监督学习设置中，The sampling ratios for the dataset were set to {5%, 10%, 20%, 50%}，3种损失函数的权重$\alpha$, $\beta$设置为0.001，在策略4）中，因为采用了3种不同的参考分布计算损失项，所以有三个kl loss权重, $\beta_{1}$, $\beta_{2}$, $\beta_{3}$，均设置为0.001。用于储存参考分布的distribution buffer中的buffer size $n$ 设置为10。

#### C.    Comparative Methods

为了验证提出方法的有效性，我们使用了一些SOTA的CD方法进行比较分析。

1）UNet [8] ：包含对称编码器和解码器，通过skip connections结合深层浅层信息的神经网络。

2）CDNet [5] ：a deconvolutional network, 基于卷积的堆叠收缩和扩展块的思想检测变化信息。

3）FC-siam-conc [6] ：特征级融合方法，使用Siamese FCN提取多级特征，并使用特征concatenation来融合双时态信息。

4）FC-siam-diff [6] ：特征级融合方法，利用Siamese FCN提取多级特征，利用特征difference来融合双时态信息。

5）SNUNet [10/24] ：a nested U-Net结构。它使用 Siamese 编码器和多个子解码器之间的密集跳跃连接来减轻深层解码器层中空间位置信息的丢失。

6）P2V [16] ：a pair-to-video change detection framework，通过a pseudo transition video将CD任务转化为视频理解任务。

7）BIT [12/22] ：一种将Transformer融入到传统卷积过程中的网络，使用传统卷积对上下文建模形成密集语义token细化原始特征。

8）LUNet [9] ：a typical convolutional and recurrent network，其中全卷积 LSTM 块配备在深度神经网络中进行端到端训练。

#### D.   Evaluation Metrics

我们使用accuracy，precision，recall，F1 score，kappa作为评价指标，分别比较4分类版本和2分类版本，为了能评估模型的综合表现，我们将4分类中的no damage 划分为2分类中的no damage，将4分类中的minor damaged，major damaged，destroyed统一划分为2分类中的damaged。这些指标的定义如下：

$$ Accuracy = \frac{TP + TN}{TP + TN + FP + FN} $$

$$ Precision = \frac{TP}{TP + FP} $$

$$ Recall = \frac{TP}{TP + FN} $$

$$ F1\ Score = \frac{2 \cdot Precision \cdot Recall}{Precision + Recall} $$

$$ Kappa = \frac{p_o - p_e}{1 - p_e} $$

$$ p_o = \frac{TP + TN}{TP + TN + FP + FN} $$

$$ p_e = \frac{(TP + FP) \cdot (TP + FN) + (FP + TN) \cdot (FN + TN)}{(TP + TN + FP + FN)^2} $$

In these formulas, TP (True Positive) represents the number of positive samples correctly predicted by the model, FP (False Positive) signifies the number of negative samples incorrectly predicted as positive, and FN (False Negative) indicates the number of positive samples incorrectly predicted as negative. $p_o$是观察到的分类一致性； $p_e$是预期的分类一致性。Note that higher F1-score, OA and Kappa point out better overall performance.

#### E.    Results and Analysis


### **V.**            **DISCUSSION**

### **VI.**            **CONCLUSION**