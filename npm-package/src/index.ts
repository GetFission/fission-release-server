import { EventEmitter } from "events"

class FissionUpdater {
  clientId : string

  constructor(id : string) {
    this.clientId = id
  }
}


// export const new FissionUpdater() : Updater



export function print(msg : String) {
  console.log("[Printing]", msg)
}
