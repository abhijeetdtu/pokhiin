import mammoth
import os , os.path
from bs4 import BeautifulSoup , NavigableString

class DocToHtml:

    @staticmethod
    def Convert(pathToFile ,fileN):
        with open(pathToFile, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
            messages = result.messages # Any messages, such as warnings during conversion


        html = html.encode("utf-8")
        html = DocToHtml.Stylize(html , fileN)
        print(fileN+".html")
        DocToHtml.WriteToPath(pathToFile.split(".")[0] +".html" , html)
        #print(soup.prettify())
        return html

    @staticmethod
    def WriteToPath(path ,string):
        f = open(path , "w")
        f.write(string.encode("utf-8"))
        f.close()

    @staticmethod
    def WriteToFile(filename , string):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)) , "../templates/Views/" , filename)
        f = open(path , "w")
        f.write(string.encode("utf-8"))
        f.close()

    
    @staticmethod
    def Stylize(htmlString  , headingString):

        htmlString = DocToHtml.CreatePanel(htmlString) 
        soup = BeautifulSoup(htmlString , 'html.parser')
        
        for x in soup.find_all("h1"):
            x['class'] = 'headingOne'

            
        for x in soup.find_all("h2"):
            x['class'] = 'headingTwo'

        for x in soup.find_all("strong"):
            x['class'] = 'headingLegible'
        for x in soup.find_all("ul"):
            x['class'] = 'list-group'

        for x in soup.find_all("li"):
            x['class'] = 'list-item'

        for x in soup.find_all("p"):
            x['class'] = 'paragraph'
        
        for x in soup.find_all("img"):
            x['class'] = 'img-thumbnail' 
        
        for x in soup.find_all("table"):
            x['class'] = 'table table-bordered'
        
        soup = DocToHtml.MakeTablesResponsive(soup)   
       
        panelBody = soup.find("div" ,{  'class' : 'panel-body'})
        text = soup.new_tag("p")
        text['class'] = 'headingMain center'
        text.append(headingString)
        panelBody.insert(0,text)
          
        return soup.prettify()

    @staticmethod
    def MakeTablesResponsive(soup):
        for x in soup.find_all("table"):
            responsiveDiv = soup.new_tag("div")
            responsiveDiv['class'] = 'table-responsive'
            x.wrap(responsiveDiv)

        return soup

    @staticmethod
    def CreatePanel(htmlString):
        htmlString = """<div class='panel panel-default'>
            <div class="panel-body">
        """.encode("utf-8") + htmlString + "</div></div>".encode("utf-8")
        #print("create panel" , htmlString)
        return htmlString


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)) , "../static/Data/abc.docx")
    print(path)
    DocToHtml.Convert(path)


