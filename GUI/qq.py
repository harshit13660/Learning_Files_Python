# # import pyglet
# # # import time
# # #
# # # animation = pyglet.image.load_animation('voice.gif')
# # # animSprite = pyglet.sprite.Sprite(animation)
# # #
# # # window = pyglet.window.Window(animSprite.width, animSprite.height)
# # #
# # #
# # # a=window.event()
# # # def on_draw():
# # #     animSprite.draw()
# # #     # time.time(3000)
# # #     # window.close()
# # #
# # # pyglet.app.run()
#
#
# def inner1(func):
#     # def inner2():
#     print("Before function execution")
#     func()
#     print("After function execution")
#     # return inner2
#
# # # @inner1
# # def function_to_be_used():
# #     print("This is inside the function")
# #
# # function_to_be_used = inner1(function_to_be_used)
# # function_to_be_used()

def ab(m):
    def b():
        print("this is me")
        m()
    return b

@ab
def c():
    print("this is we both")
c()