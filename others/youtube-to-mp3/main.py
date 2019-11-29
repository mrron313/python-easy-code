import moviepy.editor as mp
import pytube
import os
import PySimpleGUI as sg      

sg.change_look_and_feel('DarkBlue1')

layout = [[sg.Text('Youtube url')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Youtube video to mp3', layout)    

event, values = window.read()    
window.close()

video_url = values[0]
youtube = pytube.YouTube(video_url)
video = youtube.streams.filter(file_extension='mp4').first()
video.download('/home/bs0468/python-projs/python-youtube-to-mp3') 

videoName = str(video.title) + '.mp4'
mp3Name = video.title + '.mp3'

clip = mp.VideoFileClip(videoName)
clip.audio.write_audiofile(mp3Name)
os.remove(videoName)
 
sg.popup('Mp3 Coverted. Check in the folder.')
