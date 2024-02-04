from .style_template import style_list

# Create a dictionary from style_list for easier access
styles = {style['name']: (style['prompt'], style['negative_prompt']) for style in style_list}

STYLE_NAMES = [style['name'] for style in style_list]
DEFAULT_STYLE_NAME = "None"

def apply_style(style_name: str, positive: str, negative: str = "") -> tuple[str, str]:
    # Get the prompts for the given style_name, or defaults to the first style if not found
    p, n = styles.get(style_name, styles[DEFAULT_STYLE_NAME])
    return p.replace("{prompt}", positive), n + ' ' + negative

class SVD_Styler_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "a close up shot of a cappuccino steaming, on a wooden table, in a dimly lit room", "multiline": True}),
                "negative_prompt": ("STRING", {"default": "asymmetry, worst quality, low quality", "multiline": True}),
                "style_name": (STYLE_NAMES, {"default": DEFAULT_STYLE_NAME})
            }
        }

    RETURN_TYPES = ('STRING', 'STRING',)
    RETURN_NAMES = ('positive_prompt', 'negative_prompt',)
    FUNCTION = "prompt_style"
    CATEGORY = "Zho模块组/🎞️SVD"

    def prompt_style(self, style_name, prompt, negative_prompt):
        prompt, negative_prompt = apply_style(style_name, prompt, negative_prompt)
        
        return prompt, negative_prompt

NODE_CLASS_MAPPINGS = {
    "SVD_Styler_Zho": SVD_Styler_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SVD_Styler_Zho": "🎞️SVD Styler",
}
