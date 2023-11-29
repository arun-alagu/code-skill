from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    """Sign up for a user account."""

    email = StringField("Email",[Email(message="Not a valid email address."), DataRequired()]
    )
    password = PasswordField(
        "Password",
        [DataRequired(message="Please enter a password."),
        Length(min=8,message="Password should have at least 8 characters")
        ]
    )
    confirmPassword = PasswordField(
        "Repeat Password",
        [DataRequired(),
        EqualTo('password', message="Passwords must match.")
        ]
    )

    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    """Login for a user account."""

    email = StringField("Email",[Email(message="Not a valid email address."), DataRequired()]
    )
    password = PasswordField(
        "Password",
        [DataRequired(message="Please enter a password."),
        Length(min=8,message="Password should have at least 8 characters")
        ]
    )

    submit = SubmitField("Log In")


class ResetForm(FlaskForm):
    """Reset for a user account."""

    email = StringField("Email",[Email(message="Not a valid email address."), DataRequired()]
    )

    submit = SubmitField("Reset")