from .transport import Transport


@Transport.OutProfile.strain
def out_strain(self: Transport.OutProfile):
    """Assume total recrystallization during transport."""
    return 0


@Transport.duration
def duration(self: Transport):
    return self.length / self.velocity


@Transport.environment_temperature
def environment_temperature(self):
    return 293
