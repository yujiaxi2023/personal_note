一般来说是tensor size的问题
运用try和expect操作可以打印出错误
```python
class Loss(nn.Module):
    def __init__(self, args):
        super().__init__()
        self.loss_str = args.loss_str
        self.post = args.type == "post"
        self.losses = nn.ModuleList([losses[loss_fn] for loss_fn in self.loss_str.split("+")])

    def forward(self, y_pred, y_true):
        try:
            if self.post:
                device = y_pred.device
                mask = y_true > 0
                y_pred = torch.stack([y_pred[:, i][mask] for i in range(y_pred.shape[1])], 1).to(device)
                y_true = y_true[mask] - 1

            if self.loss_str == "mse":
                y_pred = F.relu(y_pred[:, 0], inplace=True)
                y_true = y_true.float()
            else:
                y_true = y_true.long()

            loss = 0
            for loss_fn in self.losses:
                loss += loss_fn(y_pred, y_true)
            return loss
        except Exception as e:
            print("Error:", e)
            print("self.post:", self.post)
            print("y_pred.shape:", y_pred.shape)
            print("y_true.shape:", y_true.shape)
            print("y_true values:", y_true)
            raise e

```
![[Pasted image 20230816021859.png]]

![[Pasted image 20230816024922.png]]
```python
def __getitem__(self, idx):  
    img_pre, _ = load_pair(self.imgs_pre[self.idx[idx]], self.lbls_pre[self.idx[idx]])  
    img_post, lbl = load_pair(self.imgs_post[self.idx[idx]], self.lbls_post[self.idx[idx]])  
    img = np.concatenate((img_pre, img_post), axis=2)  
    data = {"image": img, "mask": lbl}  
  
    try:  
        if not self.use_autoaugment:  
            data = self.zoom(image=data["image"], mask=data["mask"])  
            print("After zoom - Image shape:", data["image"].shape)  
            print("After zoom - Mask shape:", data["mask"].shape)  
  
        data = self.crop(image=data["image"], mask=data["mask"])  
        print("After crop - Image shape:", data["image"].shape)  
        print("After crop - Mask shape:", data["mask"].shape)  
  
        if self.use_autoaugment:  
            img_pre = PIL.Image.fromarray(data["image"][:, :, :3])  
            img_post = PIL.Image.fromarray(data["image"][:, :, 3:])  
            lbl = PIL.Image.fromarray(data["mask"])  
            img_pre, lbl, img_post = self.autoaugment(img_pre, lbl, img_post)  
            img_pre, img_post = np.array(img_pre), np.array(img_post)  
            data["mask"] = np.array(lbl)  
        else:  
            data = self.hflip(image=data["image"], mask=data["mask"])  
            data = self.vflip(image=data["image"], mask=data["mask"])  
            img_pre, img_post = data["image"][:, :, :3], data["image"][:, :, 3:]  
            img_pre, img_post = intensity_aug(self.noise, img_pre, img_post)  
            img_pre, img_post = intensity_aug(self.brctr, img_pre, img_post)  
        img_pre, img_post = intensity_aug(self.normalize, img_pre, img_post)  
        data["image"] = np.concatenate((img_pre, img_post), axis=2)  
        data["image"] = np.transpose(data["image"], (2, 0, 1))  
        print("Final Image shape:", data["image"].shape)  
        print("Final Mask shape:", data["mask"].shape)  
  
    except Exception as e:  
        print("An error occurred:", e)  
  
    return data
```

