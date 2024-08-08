fn main() {
    let family = std::env::var("CARGO_CFG_TARGET_FAMILY").unwrap();
    let arch = std::env::var("CARGO_CFG_TARGET_ARCH").unwrap();
    let env = std::env::var("CARGO_CFG_TARGET_ENV").unwrap();
    let target = std::env::var("TARGET").unwrap();
    if family != "windows" || arch != "x86_64" || env != "gnu" || !target.ends_with("-gnu") {
        return;
    }

    let dir = std::env::var("CARGO_MANIFEST_DIR").unwrap();

    println!("cargo:rustc-link-search=native={}", std::path::Path::new(&dir).join("lib").display());
}
