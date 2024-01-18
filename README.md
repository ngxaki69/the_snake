# [18-01-2023 TZ==MSK v=1.0]

## [authored by == Makhnach Denis]

## [global changed == true]

- class: GameObject --> base class for game objects
- class: Apple --> apple game object
- calss: Snake --> snake game object

## [new files == false]

## [new features == true]
- func: draw_cell --> method for rendering game objects in class GameObject
- func: randomize_position --> method for setting random coordinates on the field for an apple
- func: draw --> method for drawing objects (available in every child class)
- func: update_direction --> updating the direction of the snake movement
- func: move --> updating the position of each section
- func: get_head_position --> snake head coordinates
- func: reset --> resetting the snake to its initial state
- func: handle_keys(updated) --> a new way to update the snake's movement based on user clicks, added the ability to change the speed (change speed 10)
