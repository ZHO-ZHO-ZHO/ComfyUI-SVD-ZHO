![SVD11_](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO/assets/140084057/687ef467-ac9e-476a-b161-9e6f3b989220)


# ComfyUI-SVD-ZHO（WIP）

## 项目说明 | Info

- 我为 SVD 设计的 **工作流** 和 **节点** | My Workflows + Auxiliary nodes for Stable Video Diffusion (SVD) 

- **版本：0.9**    节点已经可用，标准工作流正在完善，目前仅提供预览


## 复刻 [stablevideo.com](https://stablevideo.com) 的 UI 交互 | SVD1.1 工作流设计

![Dingtalk_20240204195736](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO/assets/140084057/93ba4ae8-7dff-4084-b5b0-b60ddf34a010)


https://github.com/ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO/assets/140084057/dd0f4f25-06e1-47ee-87a4-afadfa95b921


### 与官网交互相同，提供 文生视频 和 图生视频 两种方式

- 文生视频：

    1）🎞️SVD Styler：输入提示词，选择风格（17种）

    2）🎞️SVD Aspect Ratio：选择宽高比（16:9、1:1、9:16 三种）、批次数

    3）🎞️SVD Advanced：选择步数、运动幅度、种子

    4）T2I Chooser：从生成的结果中选择一张用于生成视频

    5）生成视频（水印可选）

- 图生视频

    1）Load image：上传图像（16:9、16:9、1:1、9:16 三种）

    2）🎞️SVD Advanced：选择步数、运动幅度、种子

    3）生成视频（水印可选）

- 补充：由于官方未公开 Camera Lora 所以还未加入


## SVD1.1 辅助节点 | Nodes

![image](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO/assets/140084057/087614ee-6de9-4a64-97a5-716527303db7)


## 工作流 | Workflows

别急……


## 更新日志

- 20240204

  - V0.9 ：完成 SVD Styler，Aspect Ratio，Advanced 节点设计，初步完成标准工作流设计

  - 创建项目


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO&Date)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[stablevideo.com](https://stablevideo.com)
