import clases

persona = clases.Persona()
persona.setNombre("Felipe")
persona.setApellidos("Torres")
persona.setAltura("1.78")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("____________________________________________")

informatico = clases.Informatico()
informatico.setNombre("Felipe")
informatico.setApellidos("Torres")

print(f"El informaticos es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("________________________________________________________")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Felipe")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())