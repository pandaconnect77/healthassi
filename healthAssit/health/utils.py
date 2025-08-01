# model.py or prediction_utils.py
from torchvision import transforms
from PIL import Image
import torch
import torch.nn as nn

class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 64 * 64, 10)  # Example output: 10 classes

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 16 * 64 * 64)
        x = self.fc1(x)
        return x

def load_model():
    model = CNNModel()
    model.load_state_dict(torch.load('model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

def predict_image(image_path):
    model = load_model()

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    img = Image.open(image_path).convert('RGB')
    img_t = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_t)
        _, predicted = torch.max(output, 1)
        return predicted.item()
