import torch
import torch.nn as nn
from torch.nn import functional as F


class RecommendModel(nn.Module):
    """
    This is a model that you can input the feature and the model will tell you like or not
    """

    def __init__(
            self,
            in_dim: int,
            num_layers: int,
            embeds_dim: list,
            num_classes: int = 2,
            bias: bool = True,
            *args,
            **kwargs
    ) -> None:
        super().__init__()
        if len(embeds_dim) != num_layers:
            raise ValueError(
                "The number of layers({}) should be same as the length of embeddings dim list({}).".format(
                    num_layers, len(embeds_dim)
                )
            )
        self.bias = bias
        self.num_classes = num_classes
        self.ln = nn.Sequential()
        in_feat = in_dim
        i = 0
        for out_feat in embeds_dim:
            i += 1
            self.ln.add_module(name=f'ln{i}',
                               module=nn.Linear(in_features=in_feat, out_features=out_feat, bias=self.bias))
            self.ln.add_module(name=f'act{i}', module=nn.ReLU())
            in_feat = out_feat
        self.classifier = nn.Linear(in_features=in_feat, out_features=self.num_classes)

    def forward(self, input):
        x = input
        x = self.ln(x)
        x = self.classifier(x)
        return F.log_softmax(x, dim=1)


def load_checkpoint(path_to_checkpoint, model, optimizer=None):
    with open(path_to_checkpoint, "rb") as f:
        checkpoint = torch.load(f)
    model.load_state_dict(checkpoint['model_state'])
    if optimizer:
        optimizer.load_state_dict(checkpoint["optimizer_state"])


def save_checkpoint(model, optimizer, path_to_checkpoint, file_name):
    checkpoint = {
        'model_state': model.state_dict(),
        'optimizer_state': optimizer.state_dict(),
    }
    with open(path_to_checkpoint + file_name, "wb") as f:
        torch.save(checkpoint, f)


def build_optimizer(optim_params):
    return torch.optim.Adam(
        optim_params,
        lr=0.0002,
        betas=[0.9, 0.999],
        eps=0.0001,
        weight_decay=0.0001,
        amsgrad=False,  # optimizer_cfg['AMSGRAD'],
    )


def build_loss_fun():
    return nn.CrossEntropyLoss()


def train_step(model, optimizer, loss_fun, input, label):
    model.train()
    output = model(input)
    loss = loss_fun(output, label)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


model = RecommendModel(5, 3, [4, 2, 3])
optimizer = build_optimizer(model.parameters())
loss_fun = build_loss_fun()
input = torch.randn(3, 5, requires_grad=True)
target = torch.randint(2, (3,), dtype=torch.int64)
train_step(model, optimizer, loss_fun, input, target)
