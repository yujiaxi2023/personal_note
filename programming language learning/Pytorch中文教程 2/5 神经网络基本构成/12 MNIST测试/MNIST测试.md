![[Pasted image 20230710204349.png]]
epoch提高accuracy上升 loss下降
泛化性弱，过拟合
黄色的代表的是validation set上面的表现

```python
logits = torch.rand(4,10)

pred = F.softmax(logits, dim=1)
pred.shape
# torch.size([4,10])

pred_label = pred.argmax(dim=1)
pred_label
# tensor([9,5,9,4])

logits.argmax(dim=1)
# tensor([9,5,9,4])

label = torch.tensor([9,3,2,4])
correct = torch.eq(pred_label, label)
# tensor([1,0,0,1], dtype=torch.unit8)

correct.sum().float().item()/4.
# accuracy 0.5
```
logit是刚输出的10个节点的tensor，经过一个crossentropyloss
test的时候需要得到loss和accuracy
logits经过softmax之后变为了一个第i个节点的概率
![[Pasted image 20230710205201.png]]
取到最大值所在的位置就是argmax，这里的0.4也就是1
argmin就是取最小的位置

softmax不会改变单调性，所以取argmax没问题，因为获得的是索引
max就需要等到softmax等操作完成之后，最终值求max
这里的第一个label的返回值是 9 5 9 4 四个位置
输入的4张图片，十分类中输出的结果是9 5 9 4 这几类
这里logits做softmax得到的 pred和logits单调性不变

这里需要输入的tensor 9 3 2 4代表的是预测对的索引
correct需要计算一个equal函数 torch.eq()方法
如果相等返回1，不等返回0

item是转换为numpy值

什么时候做test
经过几次batch然后做一次test，这样是比较省compute
![[Pasted image 20230710210008.png]]
根据实际情况做test

```python
test_loss = 0
correct = 0
for data, target in test_loader:
	data = data.view(-1, 28*28)
	data, target = data.to(device), target.cuda()
	logits = net(data)
	test_loss += criteon(logits, target).item()

	pred = logits.argmax(dim=1)
	correct += pred.eq(target).float().sum().item()

test_loss /= len(test_loader.dataset)
print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(test_loss, correct, len(test_loader.dataset), 100. * correct / len(test_loader.dataset*))
```