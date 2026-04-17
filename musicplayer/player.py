import pygame
import os #for files

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init() #mixer - sound module 
        self.music_folder = music_folder #saving folver inside object
        self.playlist = self.load_tracks() #function calling and saving
        self.current_index = 0 #current track index 0 (means its firsttrack)
        self.status = "Stopped" #defolt 
        self.track_length = 1 #poka ne znayu

    def load_tracks(self): #loading tracks into playlist
        tracks = []
        for file in os.listdir(self.music_folder): #for every track in papka 
            if file.endswith(".mp3") or file.endswith(".wav"):
                tracks.append(os.path.join(self.music_folder, file)) #adds to self.music_folder
                #music + song.mp3 -> music/song.mp3
        tracks.sort()
        return tracks

    def play(self):
        if not self.playlist:
            return #if list is empty 
        track = self.playlist[self.current_index] #getting current track
        pygame.mixer.music.load(track) #music - module proigrivanya
        pygame.mixer.music.play()
        self.status = "Playing"
        
        try:
            sound = pygame.mixer.Sound(track)
            self.track_length = sound.get_length()
        except:
            self.track_length = 1

    def stop(self):
        pygame.mixer.music.stop()
        self.status = "Stopped"

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist) #next track
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist) #previous track
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks"
        return os.path.basename(self.playlist[self.current_index])
        #basename - gets just files name . music/song.mp3 -> song.mp3
        
    def get_progress(self):
        if self.status != "Playing":
            return 0
        pos_ms = pygame.mixer.music.get_pos() #getpos - position in milliseconds
        if pos_ms < 0:
            return 0
        return min(pos_ms / (self.track_length * 1000), 1) #current length/full length