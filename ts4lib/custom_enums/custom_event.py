from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomEvent(CustomEnum):
    NONE: "CustomEvent" = 'NONE'

    GLOBAL_SERVICE_START: "CustomEvent" = 'global_service.start'
    GLOBAL_SERVICE_STOP: "CustomEvent" = 'global_service.stop'

    TUNING_LOADED: "CustomEvent" = 'instance_managers.loaded'

    BUILD_BUY_ENTER: "CustomEvent" = 'build_buy.enter'
    BUILD_BUY_EXIT: "CustomEvent" = 'build_buy.exit'

    GAME_SETUP: "CustomEvent" = 'game.setup'
    GAME_LOAD: "CustomEvent" = 'game.load'
    GAME_PRE_SAVE: "CustomEvent" = 'game.pre_save'
    GAME_SAVE: "CustomEvent" = 'game.save'
    GAME_SERVICES_STARTED: "CustomEvent" = 'game_services.started'

    ZONE_LOAD: "CustomEvent" = 'zone.load'
    ZONE_STARTUP: "CustomEvent" = 'zone.startup'
    ZONE_UNLOAD: "CustomEvent" = 'zone.unload'
    ZONE_CLEANUP_OBJECTS: "CustomEvent" = 'zone.cleanup_objects'
    LOADING_SCREEN_LIFTED: "CustomEvent" = 'zone.loading_screen_lifted'
    HOUSEHOLDS_AND_SIMS_LOADED: "CustomEvent" = 'zone.all_households_and_sim_infos_loaded'

    SIM_SPAWNED: "CustomEvent" = 'sim.spawned'
    ALL_SIMS_SPAWNED: "CustomEvent" = 'sim.spawned.all'
    SIM_OUTFIT_CHANGED: "CustomEvent" = 'sim.outfit.changed'
    ACTIVE_SIM_CHANGED: "CustomEvent" = 'sim.active.changed'

    # custom injection-events
    GAME_TICK: "CustomEvent" = 'inj.game.tick-inj'
    SIM_OUTFIT_CHANGE: "CustomEvent" = 'inj.sim.outfit.changed-inj'
