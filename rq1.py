import matplotlib.pyplot as plt

dates = ['CWE-787', 'CWE-89', 'CWE-125', 'CWE-416', 'CWE-476', 'CWE-190']
guangzhou = [29.2, 27.5, 23.1, 36.4, 36.1, 31.6]
beijing = [40.3, 47.6, 33, 34.6, 62.7, 39.2]
bar_width = 0.35
index = range(len(dates))
plt.figure(figsize=(27,18))
color1 = '#808080'
color2 = '#b22222'
plt.bar(index, guangzhou, bar_width, label='SVACL', color=color1, edgecolor='black', linewidth=4, )
plt.bar([i + bar_width for i in index], beijing, bar_width, label='VulStamp', color=color2, edgecolor='black', linewidth=4,hatch='/'
        )
plt.legend(fontsize = 60)
plt.xticks([i + bar_width / 2 for i in index], dates, fontsize=80, rotation=30)
plt.yticks(fontsize=80)
plt.tight_layout()
plt.savefig('rq1.pdf', dpi=600, bbox_inches='tight')  # 保存图片，设置分辨率为300dpi，裁剪多余的边界
plt.show()




