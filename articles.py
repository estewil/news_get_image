# pip3 install newspaper3k
# Como correr el programa:
#
# python3 articles.py diario link-de-la-noticia 
# python3 articles.py infobae https://www.infobae.com/deportes/2023/09/11/el-sueno-que-cumplio-la-broma-sobre-la-esposa-de-medvedev-y-la-dedicatoria-a-kobe-bryant-el-discurso-completo-de-djokovic-tras-ganar-el-us-open/

from newspaper import Article
import sys

def get_url(diario, link):

    article = Article(url=link, language='es')
    article.download()
    article.parse()
    top_image = article.top_image
    all_images = article.images
    for image in all_images:
        match diario:
            case 'infobae':
                if "1200x630" in image:
                    break

            case 'clarin':
                if "360x240"  in image or "340x340" in image:
                    break
            
            case 'test':
                print(image)
    return image

if __name__ == "__main__":
   argumento = (sys.argv[1:])
   foto = get_url(argumento[0], argumento[1])
   print(foto)
