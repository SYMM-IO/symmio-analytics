import {NgModule} from "@angular/core"
import {RouterModule, Routes} from "@angular/router"
import {HomeComponent} from "./home/home.component"
import {EnvironmentService} from "./services/enviroment.service"
import {PanelHomeComponent} from "./panel-home/panel-home.component"

const routes: Routes = []


@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {
    constructor(environmentService: EnvironmentService) {
        if (environmentService.getValue("panel")) {
            routes.push({
                path: "home",
                component: PanelHomeComponent,
            })
        } else {
            routes.push({
                path: "home",
                component: HomeComponent,
            })
        }
    }
}
