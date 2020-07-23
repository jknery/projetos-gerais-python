'''
UNIFACISA - FACULDADE DE CIÊNCIAS SOCIAS APLICADAS
PROJETO DE INTELIGÊNCIA ARTIFICIAL
PROFª ORIENTADORA: VERA L. C. DE MEDEIROS
CLASSES QUE REALIZAM SCRAPPER EM SITES DE MUSICAS
ALUNOS: MATHEUS JORDAN PAZ | JOSÉ IVO KOERICH NERY
'''
# HTTPS:// WWW.CIFRACLUB.COM.BR
from Scrapper import Scrapper

class CifraClub(Scrapper):

    def __init__(self, url):
        super().setUrl(url)

    #Retorna um Dicionário de Artistas
    def getArtistaPorLetra(self, letra = None):

        artists = {}
        cont = 1
        while cont <= 2:

            if(letra == None):
                return "A letra é necessária!"
        
            url = "/letra/" + letra + "/lista.html"
            soap = self.makeRequest(url)
        
            body = soap.find('body')
            tbl = body.find('div', attrs={'class' : 'g-1 g-fix g-sb'})
            arts = tbl.find('ul').find_all('li')
        
            for artist in arts:
                data = artist.find('a')
                name = data.get_text()
                link = data['href']
            
                if(name[0] != letra):
                    pass
                else:
                    artists[name] = link

            cont += 1
            if letra == letra.lower(): letra = letra.upper()
            else: letra = letra.lower()

        return artists

    #Retorna um Dicionário de Nomes de Musicas
    def getMusicasPorArtistas(self, artist = None):
        if(artist == None):
            return "O nome  do Artista é necessário!"

        url = artist + "#instrument=lyrics"
        soap = self.makeRequest(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'id':'js-a-s-box'})
        mscs = tbl.find('ul', attrs={'class':'list-links art_musics alf all'}).find_all('li')
        
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
        
        url = link + '/letra/'
        soap = self.makeRequest(url)

        body = soap.find('body')
        tbl = body.find('div', attrs={'class':'g-1 g-fix cifra'})
        
        music = tbl.find('h1').get_text()
        artist = tbl.find('h2').find('a').get_text()

        lrcs = tbl.find('div', attrs={'class':'letra'}).find_all('p')

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
