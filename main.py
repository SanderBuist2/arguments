# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greet="Hello, <name>!"):
    return greet.replace("<name>", name)

def force(mass, body="earth"):
    planets = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 24.8,
        "saturn": 10.4,
        "uranus": 8.9,
        "neptune": 11.1,
        "pluto": 0.6,
        "sun": 274.0,
    }
    if (body in planets):
        return planets[body] * mass
    return 0.0

def pull(mass1, mass2, disctance):
    G = 6.674*(10**-11)
    return G * ((mass1 * mass2)/disctance**2)

print(pull(800.0, 1500.0, 3.0))

