# Generated from ed25519-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ed25519

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 2%{?dist}
Summary: An efficient digital signature library providing the Ed25519 algorithm
License: MIT
URL: https://github.com/RubyCrypto/ed25519
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release) >= 3.1
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 3.1
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/CHANGES.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/ed25519.png
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Apr 2 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.3.0-2
- Bumped up ruby lib base

* Sat Sep 10 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.3.0-1
- Initial package
