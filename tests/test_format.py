import jsonschema
import testtools
import yaml


CONTRIBUTION_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "definitions": {
        "team": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string"
                },
                "members": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "email": {
                                "type": "string"
                            }
                        },
                        "required": ["name", "email"],
                        "additionalProperties": False
                    }
                }
            },
            "required": ["description", "members"],
            "additionalProperties": False
        },
        "performed_only_if": {
            "type": "array",
            "minItems": 1,
            "items": {
                "oneOf": [
                    {
                        "type": "object",
                        "properties": {
                            "who": {"type": "string"},
                            "state": {"type": "string"}
                        },
                        "required": ["who", "state"],
                        "additionalProperties": False
                    },
                    {
                        "type": "object",
                        "properties": {
                            "OR": {
                                "$ref": "#/definitions/performed_only_if"
                            }
                        },
                        "required": ["OR"],
                        "additionalProperties": False
                    }
                ]
            }
        }
    },
    "properties": {
        "name": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "rules": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "policy": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string"
                    },
                    "performed_only_if": {
                        "$ref": "#/definitions/performed_only_if"
                    }
                },
                "required": ["action", "performed_only_if"],
                "additionalProperties": False
            }
        },
        "teams": {
            "type": "object",
            "properties": {
                "ptl": {
                    "$ref": "#/definitions/team"
                },
                "core": {
                    "$ref": "#/definitions/team"
                }
            },
            "required": ["ptl", "core"],
            "additionalProperties": False
        }
    },
    "required": ["name", "description", "rules", "policy", "teams"],
    "additionalProperties": False
}


class FormatTestCase(testtools.TestCase):

    def test_contribtuion_file(self):

        try:
            jsonschema.validate(
                yaml.safe_load(open("../CONTRIBUTION.yml").read()),
                CONTRIBUTION_SCHEMA
            )
        except Exception:
            print("File MOM-Brain/CONTRIBUTION.yml has wrong format.")
            print("Please fix it!")
            raise
