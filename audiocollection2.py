class Album:
    
    def __init__(self, name, group='Various artists'):
        self.name = name
        self.group = group
        self.track_list = []

    def __str__(self):
        tracks = [track.name + "-" + str(track.duration) + "min" for track in self.get_tracks()]
        return ('Name group: {}\nName album: {}\nTracks:\n' + '\t{}\n' * len(tracks)).format(self.group, self.name, *tracks)

    def add_track(self, track):
        self.track_list.append(track)

    def get_tracks(self):
        for track in self.track_list:
            yield track

    def get_duration(self):
        album_duration = 0
        for track in self.track_list:
            album_duration += track.duration
        print(f'{self.name.upper()} by {self.group.upper()} duration: {album_duration} min.')


class Track:
    count = 0
    
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration
        self.id = Track.count
        Track.count += 1

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def __eq__(self, other):
        return self.duration == other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __ge__(self, other):
        return self.duration >= other.duration


track_1 = Track('Let There Be More Light', 5)
track_2 = Track('Remember a Day', 4)
track_3 = Track('Set the Controls for the Heart of the Sun', 5)
track_4 = Track('Corporal Clegg', 4)
    
a_saucerful_of_secrets = Album('A Saucerful of Secrets', 'Pink Floyd')
a_saucerful_of_secrets.add_track(track_1)
a_saucerful_of_secrets.add_track(track_2)
a_saucerful_of_secrets.add_track(track_3)
a_saucerful_of_secrets.add_track(track_4)

track_5 = Track('Whole Lotta Love', 5)
track_6 = Track('What Is and What Should Never Be', 4)
track_7 = Track('The Lemon Song', 6)
track_8 = Track('Thank You', 4)

led_zeppelin_ii = Album('Led Zeppelin II', 'Led Zeppelin')
led_zeppelin_ii.add_track(track_5)
led_zeppelin_ii.add_track(track_6)
led_zeppelin_ii.add_track(track_7)
led_zeppelin_ii.add_track(track_8)

print(a_saucerful_of_secrets)
a_saucerful_of_secrets.get_duration()
print()
print('track_1: ', track_1)
print('track_2: ', track_2)
print('track_1 == track_2:', track_1 == track_2)
print('track_1 != track_2:', track_1 != track_2)
print('track_1 > track_2:', track_1 > track_2)
print('track_1 < track_2:', track_1 < track_2)
print('track_1 >= track_2:', track_1 >= track_2)
print('track_1 <= track_2:', track_1 <= track_2)
