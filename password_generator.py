import random
import string


class PasswordGenerator:
    def __init__(self, complex=True, **kwargs):
        self.complex = complex
        self.defaults = {
            'min_length': None,
            'max_length': None,
            'min_lower': None,
            'min_upper': None,
            'min_special': None,
            'min_number': None,
            'max_lower': None,
            'max_upper': None,
            'max_special': None,
            'max_number': None,
        }

        self.params = self.defaults.copy()

        for key, value in kwargs.items():
            if key in self.params and isinstance(value, int) and 0 <= value <= 100:
                self.params[key] = value

        if self.params['min_length'] and self.params['max_length'] and self.params['min_length'] > self.params['max_length']:
            raise ValueError("min_length cannot be greater than max_length")

        if self.params['min_lower'] and self.params['max_lower'] and self.params['min_lower'] > self.params['max_lower']:
            raise ValueError("min_lower cannot be greater than max_lower")

        if self.params['min_upper'] and self.params['max_upper'] and self.params['min_upper'] > self.params['max_upper']:
            raise ValueError("min_upper cannot be greater than max_upper")

        if self.params['min_special'] and self.params['max_special'] and self.params['min_special'] > self.params['max_special']:
            raise ValueError("min_special cannot be greater than max_special")

        if self.params['min_number'] and self.params['max_number'] and self.params['min_number'] > self.params['max_number']:
            raise ValueError("min_number cannot be greater than max_number")

        if self.params['max_length'] and self.params['min_lower'] and self.params['min_upper'] and self.params['min_special'] and self.params['min_number'] and (
                self.params['min_lower'] + self.params['min_upper'] +
            self.params['min_special'] + self.params['min_number']
                > self.params['max_length']):
            raise ValueError(
                "Sum of min_lower, min_upper, min_special, and min_number cannot exceed max_length")

        if self.params['min_length'] and self.params['max_lower'] and self.params['max_upper'] and self.params['max_special'] and self.params['max_number'] and (
                self.params['max_lower'] + self.params['max_upper'] +
            self.params['max_special'] + self.params['max_number']
                < self.params['min_length']):
            raise ValueError(
                "Sum of max_lower, max_upper, max_special, and max_number should have be greater than min_length")

        if self.complex:
            self.params['min_length'] = self.params['min_length'] or 12
            self.params['max_length'] = self.params['max_length'] or 16
        else:
            self.params['min_length'] = self.params['min_length'] or 8
            self.params['max_length'] = self.params['max_length'] or 12

        self.params['max_lower'] = self.params['max_lower'] or self.params['max_length'] // 3
        self.params['max_upper'] = self.params['max_upper'] or self.params['max_length'] // 3
        self.params['max_special'] = self.params['max_special'] or (self.params['max_length'] -
                                                                    self.params['max_lower'] - self.params['max_upper']) // 2
        self.params['max_number'] = self.params['max_number'] or self.params['max_length'] - \
            self.params['max_lower'] - self.params['max_upper'] - \
            self.params['max_special']

        self.params['min_lower'] = self.params['min_lower'] or self.params['min_length'] // 4
        self.params['min_upper'] = self.params['min_upper'] or self.params['min_length'] // 4
        self.params['min_special'] = self.params['min_upper'] or self.params['min_length'] // 4
        self.params['min_number'] = self.params['min_upper'] or self.params['min_length'] // 4

    def generate_password(self):
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        numeric_chars = string.digits
        special_chars = string.punctuation

        lowercase_pool = random.sample(lowercase_chars, random.randint(
            self.params['min_lower'], self.params['max_lower']))
        uppercase_pool = random.sample(uppercase_chars, random.randint(
            self.params['min_upper'], self.params['max_upper']))
        numeric_pool = random.sample(numeric_chars, random.randint(
            self.params['min_number'], self.params['max_number']))
        special_pool = random.sample(special_chars, random.randint(
            self.params['min_special'], self.params['max_special']))

        password_pool = lowercase_pool + uppercase_pool + numeric_pool + special_pool

        if self.complex:
            # Make this passwrod more complex
            random_length = random.randint(
                self.params['min_length'], self.params['max_length'])
            remaining_length = random_length - len(password_pool)

            all_chars = lowercase_chars + uppercase_chars + numeric_chars + special_chars
            password_pool.extend(random.choice(all_chars)
                                 for _ in range(remaining_length))
            random.shuffle(password_pool)

        password = ''.join(password_pool)

        return password


# Example usage
# password_generator = PasswordGenerator(
#     complex=True, min_length=10, max_length=15, min_lower=2, min_upper=2, min_special=1, min_number=1)
password_generator = PasswordGenerator()
password = password_generator.generate_password()
