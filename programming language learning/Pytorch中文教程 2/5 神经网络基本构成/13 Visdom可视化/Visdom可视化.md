TensorBoard非常好用
类似于tensorboardX是有用的
```python
import numpy as np  
from tensorboardX import SummaryWriter  
  
writer = SummaryWriter()  
writer.add_scalar('data/scalar1', dummy_s1[0], n_iter)  
writer.add_scalar(;data/scalar_group, {'xsimx': n_iter * np.sim(n_iter),  
                                       'xcosx': n_iter * np.cos(n_iter),  
                                       'arctanx': np.arctan(n_iter)}, n_iter)  
  
writer.add_image("Image", x, n_iter)  
writer.add_text("Text", 'text logged at step:' + str(n_iter), n_iter)  
  
for name, param in resnet18.named_parameters():  
    writer.add_histogram(name, param.clone().cpu().data.numpy(), n_iter)  
  
writer.close()
```
需要转换到cpu 然后转换为numpy才能进行作图

visdom相当于是一个web服务器，会监听你的模型
![[Pasted image 20230710211750.png]]
win上面一般遇到这个问题

单条曲线
```python
from visdom import Visdom  
viz = Visdom()  
viz.line([0.], [0.], win = 'train_loss', opts = dict(title = 'train loss'))  
viz.line([loss.item()], [global_step], win = 'train_loss', update = 'append')
```

多条曲线
```python
from visdom import Visdom  
viz = Visdom()  
viz.line([0.0,0.0], [0.], win = 'train_loss', opts = dict(title = 'test loss&acc', legend = ['loss','acc']))  
viz.line([[test_loss, correct / len(test_loader.dataset)]],[global_step], win = 'test', update = 'append')
```

![[Pasted image 20230710212747.png]]
