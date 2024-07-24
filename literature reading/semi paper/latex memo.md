
$$\bar{a}$$

$$
\begin{pmatrix}
a_1 & b_1 & c_1 & d_1 \\
a_2 & b_2 & c_2 & d_2 \\
\vdots & \vdots & \vdots & \vdots \\
a_n & b_n & c_n & d_n
\end{pmatrix}
$$

$$
\begin{pmatrix}
\mu_{a} & \mu_{b} & \mu_{c} & \mu_{d}
\end{pmatrix}
$$

$$D_l=\{(x_{l\_\,pre}^{\mathcal{i}}\;,\;x_{l\_\,post}^{\mathcal{i}})\;,\; y_l\}_{\mathcal{i=1}}^{M} \quad y_l\in\{0,1,2,3\}^L$$
$$\_$$
$$D_u=\{(x_{u\_\,pre}^{\mathcal{i}}\;,\;x_{u\_\,post}^{\mathcal{i}}) \}_{\mathcal{i=1}}^{N}$$

$$ e^*_t = \frac{4(\hat{\sigma}^2 + \lambda)}{(t - \hat{\mu})^2 + 2\hat{\sigma}^2 + 2\lambda} $$

$$(x_{u\_\,pre}\;,\;x_{u\_\,post})$$

$$(x_{l\_\,pre}\;,\;x_{l\_\,post})$$

$\{0,1,2,3\}$

$\hat{y}_l$

$D\sim{D_l\cup{D_u}}$

$$\mathcal{L = L_s + \alpha L_{u\underline{~}entropy} + \beta L_{u\underline{~}kl\,divergency}}$$

$$(x_{pre}\;,\;x_{post})$$

$$(x_{pre}\;,\;x_{post}) \in \mathbb{R}^{H\times{W}\times{C}}$$

$(T_pre, T_post) \in \mathbb{R}^{L^{’} \times {C}}$

$T_{new} \in \mathbb{R}^{2L^{’} \times {C}}$

$L^{’}\ll (H \times W)$

$$  
\mathbf{Q} = \mathbf{X}\mathbf{W}_Q,  
$$ $$  
\mathbf{K} = \mathbf{X}\mathbf{W}_K,  
$$ $$  
\mathbf{V} = \mathbf{X}\mathbf{W}_V,  
$$ where $\mathbf{W}_Q$, $\mathbf{W}_K$, and $\mathbf{W}_V$ are learnable weight matrices.
$$

\begin{align}

\mathbf{Q} = \mathbf{X}\mathbf{W}_q,  \\

\mathbf{K} = \mathbf{X}\mathbf{W}_k,  \\

\mathbf{V} = \mathbf{X}\mathbf{W}_v, 

\end{align}

$$

$$  
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d}}\right)\mathbf{V},  
$$

$$  
\text{MultiHead}(\mathbf{X}) = \text{Concat}(\text{head}_1, \text{head}_2, \ldots, \text{head}_h)\mathbf{W}_O,  
$$ where $\text{head}_j = \text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V})$ refers to the output of the $j$-th self-attention head.

$(T_{new\_\,pre}, T_{new\_\,post})$

MA(Xi,(l−1), Ti new ) = Concat(head1,...,headh)WO , 
	where head j = Att(Xi,(l−1)Wq j , Ti newWk j , Ti new Wv j )
$$
\begin{align}
\text{{MA}}(\mathbf{F}_{i}, \mathbf{T}, \mathbf{T}) = \text{{Concat}}(\text{{head}}_{1}, \ldots, \text{{head}}_{h}) \mathbf{W}_{O},\\
\quad where \ 
\text{{head}}_{j} = \text{{Att}}(\mathbf{F}_{i}\mathbf{W}_{qj}, \mathbf{T}\mathbf{W}_{kj}, \mathbf{T}\mathbf{W}_{vj})
\end{align}
$$

$$et(w_t, b_t, y, x_i) = (y_t - \hat{t})^2 + \frac{1}{M-1}\sum\limits_{i=1}^{M-1} (y_0 - \hat{x_i})^2$$

$$ e^*_t = \frac{4(\hat{\sigma}^2 + \lambda)}{(t - \hat{\mu})^2 + 2\hat{\sigma}^2 + 2\lambda} $$

$$\mu = \frac{1}{M} \sum_{i=1}^{M} x_i \quad$$$$ \quad \hat{\sigma}^{2} = \frac{1}{M} \sum_{i=1}^{M}(x_i - \hat{\mu})^2$$
$$ \frac{1} {e_t^{*}} $$$$ \widetilde{X} = \text{sigmoid}\left(\frac{1}{E}\right) \odot X $$

$$\text{{MSA}}(T_{sum}) = \text{{Concat}}(\text{{head}}_{1}, \ldots, \text{{head}}_{h}) W_{O}, \quad where \  \text{{head}}_{j} = \text{{Attention}}(T_{sum}W^{q}_{j}, T_{sum}W^{k}_{j}, T_{sum}W^{v}_{j})$$
