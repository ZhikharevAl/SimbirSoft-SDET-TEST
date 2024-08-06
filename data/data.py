from dataclasses import dataclass, field

from faker import Faker

fake = Faker()


@dataclass(slots=True)
class PersonData:
    first_name: str = field(default_factory=lambda: fake.first_name())
    last_name: str = field(default_factory=lambda: fake.last_name())
    email: str = field(default_factory=lambda: fake.email())
    mobile: str = field(default_factory=lambda: fake.numerify('##########'))
    current_address: str = field(default_factory=lambda: fake.address())
