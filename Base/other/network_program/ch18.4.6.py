import urllib.parse
import urllib.request
url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=2&spn=0&di=221320&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=859882613%2C1564073189&os=2505365372%2C68048922&simid=859882613%2C1564073189&adpicid=0&lpn=0&ln=1636&fr=&fmq=1640699330809_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2Ftp09%2F21052112102250D-0-lp.jpg%26refer%3Dhttp%3A%2F%2Fimg.jj20.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1643291334%26t%3D3e96b94665e3dfc82db8faf4ea52049b&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B33da_z%26e3Bv54AzdH3FprAzdH3Fnn8mla_z%26e3Bip4s&gsm=2&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCwzLDYsMSw0LDIsNSw3LDgsOQ%3D%3D'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'downlad.png'
    with open(f_name,'wb') as f:
        f.write(data)
        print('下载文件成功')