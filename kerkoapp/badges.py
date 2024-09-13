"""
Functions to add badges
"""

from kerko.specs import FieldSpec, BadgeSpec
from kerko.composer import Composer
from kerko.renderers import Renderer
from kerko.shortcuts import config


def tags_of_item(item) -> list[str]:
    """
    Returns a list of tags associated with the given item.

    :param item: The item to retrieve tags from.
    :type item: dict
    :return: A list of tags.
    :rtype: list[str]
    """

    return [tag_dic.get("tag", "") for tag_dic in item.get("data", {}).get("tags", {})]


class BadgeRenderer(Renderer):

    badge = ""

    def render(self, **context):
        return self.badge


class OABadgeRenderer(BadgeRenderer):

    badge = "<span class='badge badge-phdsio badge-open-access'>Open Access</span>"


class FT50BadgeRenderer(BadgeRenderer):

    badge = "<span class='badge badge-phdsio badge-ranking'>FT50</span>"


class UTD24BadgeRenderer(BadgeRenderer):

    badge = "<span class='badge badge-phdsio badge-ranking'>UTD24</span>"


class ABDCBadgeRenderer(BadgeRenderer):

    badge = "<span class='badge badge-phdsio badge-ranking'>A*</span>"


def add_badges(comp: Composer):
    """
    Adds badges to the given Composer object based on the specified tags.
    The required configs are assumed valid.

    Parameters:
        comp (Composer): The Composer object to which the badges will be added.
    """

    fields = comp.select_fields(["text_tags"])
    if "text_tags" not in fields:
        return

    tags: FieldSpec = fields["text_tags"]

    comp.add_badge(
        BadgeSpec(
            key="ranking-ft50",
            field=tags,
            activator=lambda _, item: config("custom.ft50_tag") in tags_of_item(item),
            renderer=FT50BadgeRenderer(),
        )
    )

    comp.add_badge(
        BadgeSpec(
            key="ranking-utd24",
            field=tags,
            activator=lambda _, item: config("custom.utd24_tag") in tags_of_item(item),
            renderer=UTD24BadgeRenderer(),
        )
    )

    comp.add_badge(
        BadgeSpec(
            key="ranking-abdc",
            field=tags,
            activator=lambda _, item: config("custom.abdc_tag") in tags_of_item(item),
            renderer=ABDCBadgeRenderer(),
        )
    )

    comp.add_badge(
        BadgeSpec(
            key="open-access",
            field=tags,
            activator=lambda _, item: config("custom.open_access_tag")
            in tags_of_item(item),
            renderer=OABadgeRenderer(),
        )
    )
