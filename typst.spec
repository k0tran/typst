Name:          typst
Version:       0.11.1
Release:       alt1
Summary:       A new markup-based typesetting system

License:       Apache-2.0
Group:         Publishing
URL:           https://typst.app
VCS:           https://github.com/typst/typst

Source0:       %name-%version.tar
Source1:       vendor-%version.tar

Patch:         typst-0.11.1-alt-bump-time-version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust libssl-devel

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%prep
%setup -a1
%patch -p1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/typst/typst-dev-assets?tag=v0.11.1"]
git = "https://github.com/typst/typst-dev-assets"
tag = "v0.11.1"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc *.md LICENSE NOTICE
%_bindir/typst

%changelog
* Thu Aug 08 2024 Ilya Sorochan <k0tran@altlinux.org>
- Initial build (closes: #50403).

