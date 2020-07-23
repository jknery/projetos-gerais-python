'''
UNIFACISA - FACULDADE DE CIÊNCIAS SOCIAS APLICADAS
PROJETO DE INTELIGÊNCIA ARTIFICIAL
PROFª ORIENTADORA: VERA L. C. DE MEDEIROS
CLASSES QUE REALIZAM SCRAPPER EM SITES DE MUSICAS
ALUNOS: MATHEUS JORDAN PAZ | JOSÉ IVO KOERICH NERY
'''
# HTTPS:// WWW.VAGALUME.COM.BR
from Scrapper import Scrapper

class Vagalume(Scrapper):

    def __init__(self, url):
        super().setUrl(url)

    #Retorna um Dicionário de Artistas
    def getArtistaPorLetra(self, letra = None):
        if(letra == None):
            return "A letra é necessária!"
        
        url = "/browse/" + letra.lower() + ".html"
        soap = self.makeRequest(url)
        
        body = soap.find('body')
        tbl = body.find('div', attrs={'class' : 'moreNamesContainer h16'})
        arts = tbl.find('ul', attrs={'class' : 'namesColumn'}).find_all('li')


        if(letra == letra.lower()): letra = letra.upper()
        
        artists = {}
        for artist in arts:
            data = artist.find('a')
            name = data.get_text()
            link = data['href']
            
            if(name[0] != letra):
                pass
            else:
                artists[name] = link

        return artists

     #Retorna um Dicionário de Musicas
    def getMusicasPorArtistas(self, artist = None):
        if(artist == None):
            return "O nome  do Artista é necessário!"

        url = artist
        soap = self.makeRequest(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'class':'topLetrasWrapper'})
        mscs = tbl.find('ol', attrs={'id':'alfabetMusicList'}).find_all('li')
        
        musics = {}
        for music in mscs:
            data = music.find('a')
            nome = data.get_text().strip()
            link = data['href']
            musics[nome] = link

        return musics
    
    #Retorna um Dicionário com a Letra da  Musica
    def getMusicas(self, link = None):
        if(link == None): return "O link do Artista e da Musica são necessários!"
        
        url = link
        soap = self.makeRequest(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'class':'cnt-head_title'})
        
        music = tbl.find('h1').get_text()
        artist = tbl.find('h2').find('a').get_text()

        tbl2 = body.find('div', attrs={'class':'cnt-letra p402_premium'})
        lrcs = tbl2.find_all('p')

        lyrics = ""
        music_info = {}
        for lyric in lrcs:

            #Replace the tags br
            lyric = str(lyric).replace('<br/>', ' ')
            lyrics += lyric

        
        #Added a paragraph
        lyrics = lyrics.replace('</p><p>', '.\n\n')

        #Remove <p> and </p> from the final of lyrics
        lyrics = lyrics.replace('<p>', '')
        lyrics = lyrics.replace('</p>', '.')

        music_info['music name'] = music
        music_info['music artist'] = artist
        music_info['music lyrics'] = lyrics

        return music_info
