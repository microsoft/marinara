// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

use tide::Request;

#[async_std::main]
async fn main() -> tide::Result<()> {
    let mut app = tide::new();
    app.at("/").get(greet);
    app.listen("0.0.0.0:8080").await?;
    Ok(())
}

async fn greet(_req: Request<()>) -> tide::Result {
    Ok(format!("Hello from the Rust server running in the Mariner Rust distroless container.").into())
}
