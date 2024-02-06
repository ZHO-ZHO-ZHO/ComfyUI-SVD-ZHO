
class SVD_Steps_MotionStrength_Seed_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "steps": ("INT", {"default": 30, "min": 25, "max": 60, "step": 1, "display": "slider"}),
                "motion_strength": ("INT", {"default": 127, "min": 1, "max": 255, "display": "slider"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT",)
    RETURN_NAMES = ("steps", "motion_strength", "seed",)
    FUNCTION = "advanced"

    CATEGORY = "Zho模块组/🎞️SVD"

    def advanced(self, steps, motion_strength, seed):
        return (steps, motion_strength, seed,)

NODE_CLASS_MAPPINGS = {
    "SVD_Steps_MotionStrength_Seed_Zho": SVD_Steps_MotionStrength_Seed_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SVD_Steps_MotionStrength_Seed_Zho": "🎞️SVD Advanced",
}
