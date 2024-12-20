import genesis as gs
gs.init(backend=gs.cpu)

print("starting scene")

scene = gs.Scene(show_viewer=True)
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)

print("building scene")

scene.build()

print("stepping into scene")

for i in range(1000):
    scene.step()