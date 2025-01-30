from orca_driver_interface.driver_interfaces import ILabwarePlaceableDriver
from typing import Any, Dict, Optional


class TestDriver(ILabwarePlaceableDriver):

    def __init__(self, name: str):
        self._name = name
        self._is_initialized = False
        self._is_running = False
        self._init_options: Dict[str, Any] = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_initialized(self) -> bool:
        return self._is_initialized

    def set_init_options(self, init_options: Dict[str, Any]) -> None:
        print(f"set_init_options: {init_options}")
        self._init_options = init_options

    async def initialize(self) -> None:
        print(f"initialized: {self._init_options}")
        self._is_initialized = True

    @property
    def is_running(self) -> bool:
        return self._is_running

    async def prepare_for_place(self, labware_name: str, labware_type: str, barcode: Optional[str] = None, alias: Optional[str] = None) -> None:
        self._is_running = True
        print(f"prepare_for_place: {labware_name}, {labware_type}, {barcode}, {alias}")
        self._is_running = False

    async def prepare_for_pick(self, labware_name: str, labware_type: str, barcode: Optional[str] = None, alias: Optional[str] = None) -> None:
        self._is_running = True
        print(f"prepare_for_pick: {labware_name}, {labware_type}, {barcode}, {alias}")
        self._is_running = False

    async def notify_picked(self, labware_name: str, labware_type: str, barcode: Optional[str] = None, alias: Optional[str] = None) -> None:
        self._is_running = True
        print(f"notify_picked: {labware_name}, {labware_type}, {barcode}, {alias}")
        self._is_running = False

    async def notify_placed(self, labware_name: str, labware_type: str, barcode: Optional[str] = None, alias: Optional[str] = None) -> None:
        self._is_running = True
        print(f"notify_placed: {labware_name}, {labware_type}, {barcode}, {alias}")
        self._is_running = False

    async def execute(self, command: str, options: Dict[str, Any]) -> None:
        self._is_running = True
        print(f"execute: {command}, {options}")
        self._is_running = False