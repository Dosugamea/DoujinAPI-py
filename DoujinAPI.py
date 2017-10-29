#encoding:utf-8
import requests
import sys
import xml.etree.ElementTree as ET

class DoujinDB():
    def __init__(self,key):
        self.API_KEY = key
        self.root = None
        self.ENDPOINT = "http://doujinshi.mugimugi.org/api/"
        self.GTI_P = "/?S=objectSearch&sn="
        self.GID_P = "/?S=getID&ID="

    def search(self,title):
        url = self.ENDPOINT + self.API_KEY + self.GTI_P + title
        try:
            data = requests.get(url).text.encode('utf-8')
            self.root = ET.fromstring(data)
            return True
        except:
            return False
            
    def get_info(self,id):
        url = self.ENDPOINT + self.API_KEY + self.GID_P + id
        try:
            data = requests.get(url).text.encode('utf-8')
            self.root = ET.fromstring(data)
            return True
        except:
            return False
            
    def create_txt(self,mode=1):
        text = ""
        if len(self.root)-1 == 1 or mode == 2:
            text += self.root[0].find("NAME_JP").text +"\n"
            text += "https://www.doujinshi.org/book/" + self.root[0].attrib["ID"][1:] + "\n\n"
            try:
                yobi = "サークル名:"
                for data in self.root[0].find("LINKS").findall('.//*[@TYPE="circle"]'):
                    yobi += " " + data.find("NAME_JP").text
                text += yobi + "\n"
            except:
                pass
            try:
                yobi = "著者名:"
                for data in self.root[0].find("LINKS").findall('.//*[@TYPE="author"]'):
                    yobi += " " + data.find("NAME_JP").text
                text += yobi + "\n"
            except:
                pass 
            text += "頒布日: "+self.root[0].find("DATE_RELEASED").text + "\n"
            text += "ページ数: "+self.root[0].find("DATA_PAGES").text + "\n"
            try:
                yobi = "原作:"
                for data in self.root[0].find("LINKS").findall('.//*[@TYPE="parody"]'):
                    yobi += " "+data.find("NAME_JP").text
                text += yobi + "\n"
            except:
                pass
            try:
                yobi = "属性:"
                for data in self.root[0].find("LINKS").findall('.//*[@TYPE="contents"]'):
                    yobi += " "+data.find("NAME_JP").text
                text += yobi + "\n"
            except:
                pass
            try:
                yobi = "キャラ:"
                for data in self.root[0].find("LINKS").findall('.//*[@TYPE="character"]'):
                    yobi += " "+data.find("NAME_JP").text
                text += yobi + "\n"
            except:
                pass
        elif len(self.root)-1 > 1:
            text = "一致する作品が複数あったため\nリンクのみを表示します\n"
            for data in self.root:
                try:
                    text += "https://www.doujinshi.org/book/"+ data.attrib["ID"][1:] + "\n"
                except:
                    pass
        else:
            txt = "その名前の作品は\n登録されていませんでした"
        return text

    def cnt(self):
        return len(self.root)-1
        
    def ids(self):
        ids = []
        for data in self.root:
            try:
                ids.append(data.attrib["ID"][1:])
            except:
                pass
        return ids
    
    def id(self):
        return self.root[0].attrib["ID"][1:]
    
    def name(self):
        return self.root[0].find("NAME_JP").text
        
    def event(self):
        return self.root[0].findall('.//*[@TYPE="convention"]')[0].find("NAME_JP").text
        
    def released(self):
        return self.root[0].find("DATE_RELEASED").text
    
    def pages(self):
        return self.root[0].find("DATA_PAGES").text
        
    def circles(self):
        circles = []
        for data in self.root[0].find("LINKS").findall('.//*[@TYPE="circle"]'):
            circles.append(data.find("NAME_JP").text)
        return circles
    
    def authors(self):
        authors = []
        for data in self.root[0].find("LINKS").findall('.//*[@TYPE="author"]'):
            authors.append(data.find("NAME_JP").text)
        return authors
    
    def parodies(self):
        parodies = []
        for data in self.root[0].find("LINKS").findall('.//*[@TYPE="parody"]'):
            parodies.append(data.find("NAME_JP").text)
        return parodies
            
    def contents(self):
        contents = []
        for data in self.root[0].find("LINKS").findall('.//*[@TYPE="contents"]'):
            contents.append(data.find("NAME_JP").text)
        return contents
        
    def characters(self):
        characters = []
        for data in self.root[0].find("LINKS").findall('.//*[@TYPE="character"]'):
            characters.append(data.find("NAME_JP").text)
        return characters
        
    def req_cnt(self):
        return self.root[1].find("Queries").text