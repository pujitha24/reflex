import reflex as rx


def test_accordion_item_style_avoids_ssr_unsafe_pseudo_class():
    style = rx.accordion.item(header="h", content="c").add_style()
    assert style is not None
    assert not any(":first-child" in key for key in style)
    assert "&:first-of-type" in style
