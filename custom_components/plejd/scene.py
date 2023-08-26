from homeassistant.components.scene import Scene

from .const import DOMAIN


async def async_setup_entry(hass, config_entry, async_add_entities):
    if config_entry.entry_id not in hass.data[DOMAIN]:
        return
    scenes = hass.data[DOMAIN][config_entry.entry_id]["scenes"]

    entities = []
    for s in scenes:
        button = PlejdScene(s, config_entry.entry_id)
        entities.append(button)
    async_add_entities(entities, False)


class PlejdScene(Scene):
    _attr_has_entity_name = True

    def __init__(self, device, entry_id):
        super().__init__()
        self.device = device
        self.entry_id = entry_id

    @property
    def name(self):
        return self.device.title

    @property
    def unique_id(self):
        return f"{self.entry_id}:{self.device.index}"

    async def async_activate(self, **kwargs):
        await self.device.activate()