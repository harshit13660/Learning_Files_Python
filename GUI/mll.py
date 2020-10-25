import pyglet
vidPath = 'voice.mp4'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()
@window.event
def on_draw():
        player.get_texture().blit(50,50)


pyglet.app.run()