import {EnvironmentInterface} from "./environment-interface"


import {environment as bnbEnv} from "./environment.bnb_8"
import {environment as ftmEnv} from "./environment.ftm_8"
import {environment as baseEnv} from "./environment.base_8"

export const environment: EnvironmentInterface = {
    name: "panel",
    assetsFolder: "panel",
    panel: true,
    environments: [
        ftmEnv,
        bnbEnv,
        baseEnv,
    ],
}