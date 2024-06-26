# Generated from rubyntlm-0.6.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubyntlm

Name: rubygem-%{gem_name}
Version: 0.6.3
Release: 1%{?dist}
Summary: Ruby/NTLM library
License: MIT
URL: https://github.com/winrb/rubyntlm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
# BuildRequires: rubygem(github_changelog_generator) = 1.14.3
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(rspec) >= 2.11
# BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
Ruby/NTLM provides message creator and parser for the NTLM authentication.


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



%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/rubyntlm.gemspec
%{gem_instdir}/spec

%changelog
* Sun Sep 11 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.6.3-1
- Initial package
