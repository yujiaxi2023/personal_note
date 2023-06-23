import torch
from torch import nn
from torch.nn import functional as F
from torch import optim

import torchvision
from matplotlib import pyplot as plt

from utils import plot_image, plot_curve, one_hot

batch_size = 512
# step1. load dataset 加载 Mnist数据集指定我们数据做train和test
# 把numpy格式转换为torch使用的tensor格式
# 正则化数据 shuffle是加载的时候做随机打散 batch是每次加载多少图片
# 这样就完成了数据的加载和batch shuffle normalization 转换为tensor等处理
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist data', train=True, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081)
                                   )
                               ])),
    batch_size=batch_size, shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist data', train=False, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,)
                                   )
                               ])),
    batch_size=batch_size, shuffle=False
)

x, y = next(iter(train_loader))
print(x.shape, y.shape, x.min(), x.max())
# 注释掉正则化行会让张量最小最大值变化位0和1
plot_image(x, y, 'image sample')


# 进行三层线性方程嵌套 网络的构建
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # wx+b
        self.fc1 = nn.Linear(28 * 28, 256)  # 第一层的784是根据像素决定的
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 10)  # 最后一层是按照十分类这个条件决定的

    def forward(self, x):
        # x: [b, 1, 28, 28]
        # h1 = relu(w1x + b1)
        x = F.relu(self.fc1(x))
        # h2 = relu(w2h1 + b2)
        x = F.relu(self.fc2(x))
        # h3 = w3h2 + b3
        x = self.fc3(x)

        return x


# 进行网络训练
net = Net()
# [w1, b1, w2, b3, w3, b3] momentum是动量
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.5)

train_loss = []

for epoch in range(3):

    for batch_idx, (x, y) in enumerate(train_loader):
        # x: torch.Size([512, 1, 28, 28]) torch.Size([512])
        # print(x.shape, y.shape)
        # [b, 1, 28, 28] => [b, feature] 这里x的tensor是四维的 需要先降成二维的tensor
        x = x.view(x.size(0), 28 * 28)
        # => [b, 10] 从[b, 784]可以变化为[b, 10]的样子
        out = net(x)
        # [b, 10]
        y_onehot = one_hot(y)
        # loss = mse(out, y_onehot)
        loss = F.mse_loss(out, y_onehot)

        loss.backward()
        # w' = w - lr*grad
        optimizer.step()

        train_loss.append(loss.item())

        if batch_idx % 10 == 0:
            print(epoch, batch_idx, loss.item())

plot_curve(train_loss)
# 得到一个比较好的[w1, b1, w2, b2, w3, b3]

total_correct = 0
for x, y in test_loader:
    x = x.view(x.size(0), 28 * 28)
    out = net(x)
    # out: [b, 10] 输出的是最大值所在的索引位置 => pred: [b]
    pred = out.argmax(dim=1)
    correct = pred.eq(y).sum().float().item()
    total_correct += correct

total_num = len(test_loader.dataset)
acc = total_correct / total_num
print('test acc:', acc)  # 得到总的accuracy

x, y = next(iter(test_loader))
out = net(x.view(x.size(0), 28*28))
pred = out.argmax(dim=1)
plot_image(x, pred, 'test')
