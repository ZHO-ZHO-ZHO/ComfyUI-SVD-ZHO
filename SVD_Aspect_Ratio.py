import torch

class SVD_Aspect_Ratio_Zho:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "Aspect_Ratio":  (["16:9", "1:1", "9:16"],),"batch_size": ("INT", {"default": 1, "min": 1, "max": 64})}}

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "latent_ratio"

    CATEGORY = "Zho模块组/🎞️SVD"

    def latent_ratio(self, Aspect_Ratio, batch_size=1):

        if Aspect_Ratio == "16:9":
            width, height = 1368, 768
        elif Aspect_Ratio == "1:1":
            width, height = 1024, 1024
        elif Aspect_Ratio == "9:16":
            width, height = 768, 1368
        else:
            raise ValueError("Unsupported Aspect Ratio")

        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples":latent}, )

NODE_CLASS_MAPPINGS = {
    "SVD_Aspect_Ratio_Zho": SVD_Aspect_Ratio_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SVD_Aspect_Ratio_Zho": "🎞️SVD Aspect Ratio",
}
