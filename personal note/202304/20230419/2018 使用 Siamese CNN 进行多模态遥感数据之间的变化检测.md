![[1807.09562.pdf]]
这篇文章介绍了一种使用 Siamese CNN 检测多模态遥感数据之间变化的方法。该方法通过将 3D 激光扫描点云和 2D 图像转换为图像块，然后使用 Siamese CNN 来检测建筑物和树木的变化。实验结果表明，该方法能够准确地检测出建筑物和树木的变化，并且能够区分真实变化和由于数据问题造成的虚假变化。

[Siamese CNN 是一种神经网络架构，它包含两个或更多相同的子网络。这里的“相同”意味着它们具有相同的配置、参数和权重。Siamese CNN 能够学习一种度量，用于比较两个输入之间的相似性。它们常用于诸如人脸识别、签名验证和药丸识别等实际应用中。此外，由于 Siamese CNN 可以使用极少的数据进行训练，因此它们也可以用于一次性学习和少量学习等更高级的应用](https://pyimagesearch.com/2020/11/30/siamese-networks-with-keras-tensorflow-and-deep-learning/) [1](https://pyimagesearch.com/2020/11/30/siamese-networks-with-keras-tensorflow-and-deep-learning/)[2](https://builtin.com/machine-learning/siamese-network)。

根据文章中的描述，该模型在荷兰恩斯赫德市的城市数据上进行了测试。结果表明，Siamese CNN 模型能够区分真实的建筑物和树木变化与由于数据问题造成的假变化。测试精度为 86.4%，准确率为 79.9%，召回率为 80.6%。