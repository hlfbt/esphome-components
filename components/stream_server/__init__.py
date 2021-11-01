# Copyright (C) 2021 Oxan van Leeuwen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_PORT

# ESPHome doesn't know the Stream abstraction yet, so hardcode to use a UART for now.

DEPENDENCIES = ["uart"]

MULTI_CONF = True

CONF_MAX_CLIENTS = "max_clients"
CONF_HELLO_MESSAGE = "hello_message"

StreamServerComponent = cg.global_ns.class_("StreamServerComponent", cg.Component)

CONFIG_SCHEMA = (
	cv.Schema(
		{
			cv.GenerateID(): cv.declare_id(StreamServerComponent),
			cv.Optional(CONF_PORT): cv.port,
			cv.Optional(CONF_MAX_CLIENTS): cv.int_range(min=-4, max=4),
			cv.Optional(CONF_HELLO_MESSAGE): cv.string
		}
	)
		.extend(cv.COMPONENT_SCHEMA)
		.extend(uart.UART_DEVICE_SCHEMA)
)

def to_code(config):
	var = cg.new_Pvariable(config[CONF_ID])
	if CONF_PORT in config:
		cg.add(var.set_port(config[CONF_PORT]))
	if CONF_MAX_CLIENTS in config:
		cg.add(var.set_max_clients(config[CONF_MAX_CLIENTS]))
	if CONF_HELLO_MESSAGE in config:
		cg.add(var.set_hello_message(config[CONF_HELLO_MESSAGE]))

	yield cg.register_component(var, config)
	yield uart.register_uart_device(var, config)
