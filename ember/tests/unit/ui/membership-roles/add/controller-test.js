import { setupTest } from "ember-qunit";
import { module, test } from "qunit";

module("Unit | Controller | membership-roles/add", function (hooks) {
  setupTest(hooks);

  test("it exists", function (assert) {
    const controller = this.owner.lookup("controller:membership-roles/add");
    assert.ok(controller);
  });
});
